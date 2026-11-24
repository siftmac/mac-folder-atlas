#!/usr/bin/env python3
"""Regenerate the Mac Folder Atlas from the siftmac.com page sources.

Every answer is written once, as a page source in the SiftMac repo
(seo/content/safe-to-delete/<id>.json), which also builds https://siftmac.com/safe-to-delete/<id>.
This script turns those sources into the Atlas, so the two never drift apart:

  atlas.json              every folder, one record each
  atlas.csv               the same records, flattened for spreadsheets
  ATLAS.md                a table to browse, grouped by category
  bin/folder-atlas        the command, built from src/folder-atlas.sh with the data inside
  raycast/src/atlas.json  the copy the Raycast extension ships with
  test/cases.tsv          path → id cases for test/test.sh

Usage:
  python3 scripts/sync.py --source ../SiftMac          write everything
  python3 scripts/sync.py --source ../SiftMac --check  change nothing; exit 1 if a file is out of date

Only the standard library; Python 3.9 or later.
"""
import argparse
import csv
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://siftmac.com"
KIND = "safe-to-delete"
REPO = "https://github.com/siftmac/mac-folder-atlas"
CLI = "folder-atlas"

# As the app and the site word them (VERDICTS in the site's build), with what each one means.
VERDICTS = {
    "rebuilds": ("Rebuilds", "Comes back by itself. Clearing it costs time or a download, not your data."),
    "safe": ("Safe", "Logs and leftovers nobody needs."),
    "decide": ("You decide", "Yours to judge: it doesn't come back, or only by downloading or making it again."),
    "leave": ("Leave it", "Leave it to macOS or the app."),
}
# The order of the site's hub page.
CATEGORIES = ["Library and system", "macOS files", "Apple apps", "Apps", "Browsers", "Creative apps", "Games",
              "Developer tools", "Project folders", "Package caches", "AI tools", "Virtual machines"]

LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
EM = re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])")
ERE_SPECIAL = set("\\.[](){}*+?^$|")

problems = []


def fail(where, msg):
    problems.append(f"{where}: {msg}")


# ---------- text ----------

def absolute_links(md):
    """Site-relative links become full siftmac.com links, so they work wherever the text goes."""
    return LINK.sub(lambda m: f"[{m.group(1)}]({SITE + m.group(2) if m.group(2).startswith('/') else m.group(2)})", md)


def outside_code(md, fn):
    parts = re.split(r"(`[^`]+`)", md)
    return "".join(p if p.startswith("`") and p.endswith("`") and len(p) > 1 else fn(p) for p in parts)


def term(md):
    """Markdown for the terminal: links become their text, *em* goes plain; **bold** and `code` stay as marks."""
    return outside_code(LINK.sub(r"\1", md), lambda s: EM.sub(r"\1", s))


def plain(md):
    return re.sub(r"[`*]", "", LINK.sub(r"\1", md))


def sentences(md):
    """Split a Markdown paragraph into sentences, not counting full stops inside `code`."""
    out, start, tick, i = [], 0, False, 0
    while i < len(md):
        ch = md[i]
        if ch == "`":
            tick = not tick
        elif ch in ".?!" and not tick:
            j = i + 1
            while md[j:j + 2] == "**":
                j += 2
            if j >= len(md) or md[j] == " ":
                out.append(md[start:j].strip())
                start = i = j
                continue
        i += 1
    if md[start:].strip():
        out.append(md[start:].strip())
    return out


def lead(md):
    """The first sentence, or the first two when the first is only a word or three ("**Yes.**")."""
    ss = sentences(md)
    if len(ss) > 1 and len(plain(ss[0]).split()) <= 3:
        return ss[0] + " " + ss[1]
    return ss[0] if ss else md


def blocks_md(blocks):
    out = []
    for b in blocks:
        if "p" in b:
            out.append(absolute_links(b["p"]))
        elif "ul" in b:
            out.append("\n".join(f"- {absolute_links(i)}" for i in b["ul"]))
        elif "ol" in b:
            out.append("\n".join(f"{n}. {absolute_links(i)}" for n, i in enumerate(b["ol"], 1)))
        elif "code" in b:
            out.append(f"```\n{b['code']}\n```")
        elif "h3" in b:
            out.append(f"### {b['h3']}")
        elif "table" in b:
            t = b["table"]
            rows = [t["head"], ["---"] * len(t["head"])] + t["rows"]
            out.append("\n".join("| " + " | ".join(absolute_links(c) for c in r) + " |" for r in rows))
        elif "note" in b:
            out.append("> " + absolute_links(b["note"]))
        else:
            fail("blocks", f"unknown block {list(b)}")
    return "\n\n".join(out)


def blocks_term(blocks):
    """The same blocks as (type, text) lines for `folder-atlas --more`."""
    out = []
    for b in blocks:
        if "p" in b:
            out.append(("p", term(b["p"])))
        elif "ul" in b:
            out += [("li", "- " + term(i)) for i in b["ul"]]
        elif "ol" in b:
            out += [("li", f"{n}. " + term(i)) for n, i in enumerate(b["ol"], 1)]
        elif "code" in b:
            out += [("code", line) for line in b["code"].split("\n")]
        elif "h3" in b:
            out.append(("h3", term(b["h3"])))
        elif "table" in b:
            out += [("li", "- " + ": ".join(term(c) for c in row)) for row in b["table"]["rows"]]
        elif "note" in b:
            out.append(("p", term(b["note"])))
    return out


# ---------- match rules ----------

def path_glob(path):
    """A page's path, as written for people, to a glob: <project>/x matches x anywhere, <ID> any one name."""
    g = path.rstrip("/").replace("…", "**")
    if re.match(r"<(project|package)>/", g):
        g = "**/" + g.split("/", 1)[1]
    g = re.sub(r"^/Volumes/(MyDrive|<drive>)/", "/Volumes/*/", g)
    g = re.sub(r"<[^>]+>", "*", g)
    g = g.replace("**/**/", "**/")
    if not g.startswith(("/", "~", "**/")):
        g = "**/" + g
    return g


def ere(text):
    return "".join("\\" + c if c in ERE_SPECIAL else c for c in text)


def glob_rule(glob):
    """A glob to what the command needs: anchor, needle, weight and an ERE for awk.

    anchor is "~" (the regex follows a home folder the command puts in front), "/" (from the root)
    or "*" (anywhere: one path component onwards). A path matches when it is the folder or inside it.
    """
    if glob.startswith("**/"):
        anchor, body = "*", glob[3:]
    elif glob.startswith("~/"):
        anchor, body = "~", glob[1:]
    elif glob.startswith("/"):
        anchor, body = "/", glob
    else:
        raise ValueError(f"bad glob {glob!r}")
    comps = [c for c in body.split("/") if c]
    rx = ""
    for i, c in enumerate(comps):
        if c == "**":
            rx += "(/[^/]+)*"
            continue
        part = "".join("[^/]*" if ch == "*" else ere(ch) for ch in c)
        rx += ("/" if (anchor != "*" or i > 0) else "") + part
    rx = {"*": "(^|/)", "/": "^", "~": ""}[anchor] + rx + "(/|$)"
    literal = ("/" if anchor == "*" else "") + body
    runs = [r for r in re.split(r"\*+", literal) if r]
    needle = max(runs, key=len) if runs else ""
    weight = len(literal.replace("*", ""))
    return anchor, needle, weight, rx


# ---------- read ----------

def load(source, extra):
    content = source / "seo" / "content" / KIND
    if not content.is_dir():
        sys.exit(f"sync: no {content}. Point --source at a SiftMac checkout.")
    dates_file = source / "seo" / "dates.json"
    dates = json.loads(dates_file.read_text(encoding="utf-8")) if dates_file.exists() else {}
    files = sorted(content.glob("*.json"))
    ids = {f.stem for f in files}
    by_path = extra.get("paths", {})
    used_paths = set()
    seen_globs = {}
    records = []
    for f in files:
        sid = f.stem
        page = json.loads(f.read_text(encoding="utf-8"))
        where = f"{KIND}/{sid}"
        for key in ("short", "h1", "category", "verdict", "paths", "summary", "sections", "sources"):
            if not page.get(key):
                fail(where, f"missing {key}")
        if problems:
            continue
        if page["verdict"] not in VERDICTS:
            fail(where, f"unknown verdict {page['verdict']!r}")
            continue
        sections = {s["id"]: s for s in page["sections"]}
        for sec in ("what", "size", "delete"):
            if sec not in sections:
                fail(where, f"no {sec!r} section")
        if problems:
            continue
        summary = [absolute_links(s) for s in page["summary"]]
        if len(summary) != 3 or not summary[2].startswith("**Does it come back?**"):
            fail(where, "summary should be: answer, trade-off, “Does it come back?”")
            continue
        comes_back = summary[2][len("**Does it come back?**"):].strip()
        what = next((absolute_links(b["p"]) for b in sections["what"]["blocks"] if "p" in b), "")
        measure = [b["code"] for b in sections["size"]["blocks"] if "code" in b]
        clear_blocks = sections["delete"]["blocks"]
        rules = []
        for p in page["paths"]:
            g = path_glob(p)
            rule = {"glob": g}
            if p in by_path:
                rule.update(by_path[p])
                used_paths.add(p)
            rules.append(rule)
        rules += [dict(r) for r in extra.get("extra", {}).get(sid, [])]
        uniq = []
        for r in rules:
            unknown = set(r) - {"glob", "beside", "has", "verdict", "note"}
            if unknown:
                fail(where, f"rule {r['glob']}: unknown keys {sorted(unknown)}")
            if "verdict" in r and r["verdict"] not in VERDICTS:
                fail(where, f"rule {r['glob']}: unknown verdict {r['verdict']!r}")
            if ("verdict" in r) != ("note" in r):
                fail(where, f"rule {r['glob']}: a verdict of its own needs a note saying why, and the other way round")
            if r["glob"] in [u["glob"] for u in uniq]:
                continue
            other = seen_globs.get(r["glob"])
            if other and other != sid:
                fail(where, f"{r['glob']} is also a path of {other}")
            seen_globs[r["glob"]] = sid
            try:
                glob_rule(r["glob"])
            except ValueError as e:
                fail(where, str(e))
            uniq.append(r)
        date = dates.get(f"/{KIND}/{sid}", {})
        see_also = [r.split("/")[2].split("#")[0] for r in page.get("related", []) if r.startswith(f"/{KIND}/")]
        for s in see_also:
            if s not in ids:
                fail(where, f"related page {s} isn't in the Atlas")
        label, _ = VERDICTS[page["verdict"]]
        records.append({
            "id": sid,
            "name": page["short"],
            "question": page["h1"],
            "category": page["category"],
            "paths": page["paths"],
            "verdict": page["verdict"],
            "verdict_label": label,
            "answer": lead(summary[0]),
            "summary": summary,
            "comes_back": comes_back,
            "what": what,
            "measure": measure,
            "how_to_clear": blocks_md(clear_blocks),
            "clear_commands": [b["code"] for b in clear_blocks if "code" in b],
            "sources": [{"title": s["title"], "url": s["url"]} for s in page["sources"]],
            "see_also": see_also,
            "match": uniq,
            "url": f"{SITE}/{KIND}/{sid}",
            "markdown_url": f"{SITE}/{KIND}/{sid}.md",
            "published": date.get("published"),
            "updated": date.get("modified"),
            "_term": {
                "answer": term(lead(summary[0])),
                "back": term(lead(comes_back)),
                "summary": [term(s) for s in summary],
                "measure": measure,
                "clear": blocks_term(clear_blocks),
            },
        })
    for p in by_path:
        if p not in used_paths:
            fail("scripts/match.json", f"rule for {p!r}, which no page lists")
    for sid in extra.get("extra", {}):
        if sid not in ids:
            fail("scripts/match.json", f"extra rules for {sid!r}, which isn't a page")
    return records


def ordered(records):
    def key(r):
        c = r["category"]
        return (CATEGORIES.index(c) if c in CATEGORIES else len(CATEGORIES), c.lower(), r["name"].lower())
    return sorted(records, key=key)


# ---------- write ----------

def public(r):
    return {k: v for k, v in r.items() if not k.startswith("_")}


def atlas_json(records):
    updated = max((r["updated"] or "" for r in records), default="")
    doc = {
        "name": "Mac Folder Atlas",
        "description": "Is it safe to delete this folder on a Mac? A verdict, a short answer and how to clear it, "
                       "for the folders and files that fill Macs.",
        "homepage": REPO,
        "license": "CC-BY-4.0",
        "credit": "Mac Folder Atlas (siftmac.com)",
        "updated": updated,
        "count": len(records),
        "verdicts": {k: {"label": v[0], "means": v[1]} for k, v in VERDICTS.items()},
        "folders": [public(r) for r in sorted(records, key=lambda r: r["id"])],
    }
    return json.dumps(doc, indent=1, ensure_ascii=False) + "\n"


def atlas_csv(records):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["id", "name", "category", "verdict", "verdict_label", "paths", "answer", "comes_back", "url",
                "updated"])
    for r in sorted(records, key=lambda r: r["id"]):
        w.writerow([r["id"], r["name"], r["category"], r["verdict"], r["verdict_label"], "; ".join(r["paths"]),
                    plain(r["answer"]), plain(r["comes_back"]), r["url"], r["updated"] or ""])
    return buf.getvalue()


def cell(text):
    return text.replace("|", "\\|")


def atlas_md(records):
    counts = {k: sum(1 for r in records if r["verdict"] == k) for k in VERDICTS}
    out = [
        "# The Mac Folder Atlas",
        "",
        f"{len(records)} folders and files that fill Macs, each with a verdict, a short answer and a link to the "
        "full answer: what it is, how big it gets, how to clear it safely and what happens afterwards.",
        "",
        "| Verdict | Means | Folders |",
        "|---|---|---|",
    ]
    out += [f"| **{v[0]}** | {v[1]} | {counts[k]} |" for k, v in VERDICTS.items()]
    out += ["", "Made from [`atlas.json`](atlas.json) by `scripts/sync.py`. To fix an answer, open an issue; "
                "this file is regenerated, not edited.", ""]
    groups = {}
    for r in ordered(records):
        groups.setdefault(r["category"], []).append(r)
    out.append("**Categories:** " + " · ".join(
        f"[{c}](#{re.sub(r'[^a-z0-9]+', '-', c.lower()).strip('-')})" for c in groups))
    for c, rs in groups.items():
        out += ["", f"## {c}", "", "| Folder | Where | Verdict | Short answer |", "|---|---|---|---|"]
        for r in rs:
            where = "<br>".join(f"`{p}`" for p in r["paths"])
            out.append(f"| [{cell(r['name'])}]({r['url']}) | {cell(where)} | {r['verdict_label']} "
                       f"| {cell(r['answer'])} |")
    out.append("")
    out.append("Data: [CC BY 4.0](LICENSE-DATA). Credit “Mac Folder Atlas (siftmac.com)” and link the entry’s page.")
    out.append("")
    return "\n".join(out)


def tsv(*fields):
    for f in fields:
        if "\t" in f or "\n" in f:
            raise ValueError(f"tab or newline in {f!r}")
    return "\t".join(fields)


def cli_data(records):
    lines = []
    for r in ordered(records):
        t = r["_term"]
        lines.append(tsv("F", r["id"], r["verdict"], r["verdict_label"], r["name"], r["category"], r["url"],
                         t["answer"], t["back"], r["match"][0]["glob"],
                         " ".join([r["id"], r["name"], r["category"]] + r["paths"])))
    for r in ordered(records):
        for m in r["match"]:
            anchor, needle, weight, rx = glob_rule(m["glob"])
            v = m.get("verdict", "")
            lines.append(tsv("M", r["id"], anchor, needle, str(weight), rx, m.get("beside", ""), m.get("has", ""),
                             m["glob"], v, VERDICTS[v][0] if v else "", term(m.get("note", ""))))
    for r in ordered(records):
        t = r["_term"]
        x = [("p", s) for s in t["summary"]]
        if t["measure"]:
            x.append(("h", "Measure it"))
            for block in t["measure"]:
                x += [("code", line) for line in block.split("\n")]
        x.append(("h", "How to clear it"))
        x += t["clear"]
        x.append(("h", "Sources"))
        x += [("src", f"{s['title']}: {s['url']}") for s in r["sources"]]
        lines += [tsv("X", r["id"], kind, text) for kind, text in x]
    for r in ordered(records):
        lines.append(tsv("J", r["id"], json.dumps(public(r), ensure_ascii=False, separators=(",", ":"))))
    return "\n".join(lines)


def cli_script(records, template):
    data = cli_data(records)
    if "\nATLAS_DATA\n" in "\n" + data + "\n":
        raise ValueError("data contains the heredoc delimiter")
    updated = max((r["updated"] or "" for r in records), default="")
    return (template.replace("@@DATA_DATE@@", updated)
                    .replace("@@COUNT@@", str(len(records)))
                    .replace("@@DATA@@", data))


def test_cases(records):
    """Every concrete path on a page should look up to that page (placeholders and wildcards skipped)."""
    lines = ["# path\texpected id (generated by scripts/sync.py; ~ is the home folder)"]
    for r in sorted(records, key=lambda r: r["id"]):
        for p in r["paths"]:
            if re.search(r"[<>…*]", p) or "MyDrive" in p:
                continue
            lines.append(f"{p.rstrip('/')}\t{r['id']}")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--source", default=str(ROOT.parent / "SiftMac"), help="a SiftMac checkout (default ../SiftMac)")
    ap.add_argument("--check", action="store_true", help="write nothing; exit 1 if any file is out of date")
    args = ap.parse_args()

    extra = json.loads((ROOT / "scripts" / "match.json").read_text(encoding="utf-8"))
    records = load(Path(args.source).expanduser().resolve(), extra)
    if problems:
        print("sync: the page sources need fixing first:", *problems, sep="\n  ", file=sys.stderr)
        return 1

    template = (ROOT / "src" / f"{CLI}.sh").read_text(encoding="utf-8")
    raycast = ROOT / "raycast" / "src" / "atlas.json"
    outputs = {
        ROOT / "atlas.json": atlas_json(records),
        ROOT / "atlas.csv": atlas_csv(records),
        ROOT / "ATLAS.md": atlas_md(records),
        ROOT / "bin" / CLI: cli_script(records, template),
        ROOT / "test" / "cases.tsv": test_cases(records),
    }
    if raycast.parent.is_dir():
        outputs[raycast] = atlas_json(records)

    stale = []
    for path, text in outputs.items():
        old = path.read_text(encoding="utf-8") if path.exists() else None
        if old == text:
            continue
        stale.append(path.relative_to(ROOT))
        if not args.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
    (ROOT / "bin" / CLI).chmod(0o755) if (ROOT / "bin" / CLI).exists() else None

    counts = {k: sum(1 for r in records if r["verdict"] == k) for k in VERDICTS}
    summary = ", ".join(f"{n} {VERDICTS[k][0].lower()}" for k, n in counts.items())
    if args.check:
        if stale:
            print("sync: out of date:", *stale, sep="\n  ", file=sys.stderr)
            return 1
        print(f"sync: up to date ({len(records)} folders: {summary})")
        return 0
    print(f"sync: {len(records)} folders ({summary}); "
          + (f"wrote {', '.join(map(str, stale))}" if stale else "nothing changed"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
