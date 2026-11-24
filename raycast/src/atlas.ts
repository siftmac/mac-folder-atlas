import { statSync } from "fs";
import { homedir } from "os";
import { dirname, join } from "path";
import bundled from "./atlas.json";

export type Verdict = "rebuilds" | "safe" | "decide" | "leave";

export interface Rule {
  glob: string;
  beside?: string;
  has?: string;
  verdict?: Verdict;
  note?: string;
}

export interface Folder {
  id: string;
  name: string;
  question: string;
  category: string;
  paths: string[];
  verdict: Verdict;
  verdict_label: string;
  answer: string;
  summary: string[];
  comes_back: string;
  what?: string;
  measure?: string[];
  how_to_clear: string;
  clear_commands?: string[];
  sources: { title: string; url: string }[];
  see_also?: string[];
  match: Rule[];
  url: string;
  markdown_url?: string;
  updated?: string | null;
}

export interface Atlas {
  name: string;
  updated: string;
  count: number;
  verdicts: Record<Verdict, { label: string; means: string }>;
  folders: Folder[];
}

/** The copy that ships with the extension. The commands also fetch the latest from GitHub. */
export const BUNDLED = bundled as unknown as Atlas;
export const ATLAS_URL = "https://raw.githubusercontent.com/siftmac/mac-folder-atlas/main/atlas.json";
export const REPO_URL = "https://github.com/siftmac/mac-folder-atlas";

/** The site's hub order. */
export const CATEGORIES = [
  "Library and system",
  "macOS files",
  "Apple apps",
  "Apps",
  "Browsers",
  "Creative apps",
  "Games",
  "Developer tools",
  "Project folders",
  "Package caches",
  "AI tools",
  "Virtual machines",
];

export interface Match {
  folder: Folder;
  /** The absolute path that was looked up. */
  path: string;
  /** The known folder it matched: the path itself, or a folder it is inside. */
  matched: string;
  inside: boolean;
  /** The verdict for the matched folder: the entry's, or the rule's own for a folder the page treats differently. */
  verdict: Verdict;
  label: string;
  note?: string;
}

interface Compiled {
  folder: Folder;
  rule: Rule;
  anchor: "~" | "/" | "*";
  source: string;
  needle: string;
  weight: number;
}

const LABELS: Record<Verdict, string> = { rebuilds: "Rebuilds", safe: "Safe", decide: "You decide", leave: "Leave it" };

function escapeRe(s: string): string {
  return s.replace(/[\\^$.*+?()[\]{}|]/g, "\\$&");
}

/** A glob from atlas.json to a regular expression: the same rules as the folder-atlas command. */
function compile(folder: Folder, rule: Rule): Compiled {
  const g = rule.glob;
  const anchor = g.startsWith("**/") ? "*" : g.startsWith("~/") ? "~" : "/";
  const body = anchor === "*" ? g.slice(3) : anchor === "~" ? g.slice(1) : g;
  let rx = "";
  body
    .split("/")
    .filter(Boolean)
    .forEach((c, i) => {
      if (c === "**") {
        rx += "(/[^/]+)*";
        return;
      }
      const part = [...c].map((ch) => (ch === "*" ? "[^/]*" : escapeRe(ch))).join("");
      rx += (anchor !== "*" || i > 0 ? "/" : "") + part;
    });
  const source = (anchor === "*" ? "(^|/)" : anchor === "/" ? "^" : "") + rx + "(/|$)";
  const literal = (anchor === "*" ? "/" : "") + body;
  const needle = literal
    .split(/\*+/)
    .filter(Boolean)
    .reduce((a, b) => (b.length > a.length ? b : a), "");
  return { folder, rule, anchor, source, needle, weight: literal.replace(/\*/g, "").length };
}

const cache = new WeakMap<Atlas, Compiled[]>();

function rules(atlas: Atlas): Compiled[] {
  let list = cache.get(atlas);
  if (!list) {
    list = atlas.folders.flatMap((f) => f.match.map((r) => compile(f, r)));
    cache.set(atlas, list);
  }
  return list;
}

function isFile(path: string): boolean {
  try {
    return statSync(path).isFile();
  } catch {
    return false;
  }
}

export function exists(path: string): boolean {
  try {
    statSync(path);
    return true;
  } catch {
    return false;
  }
}

/** A path as typed to a clean absolute one: ~, /var, /tmp and the Data volume's own paths. */
export function normalize(input: string): string {
  const home = homedir();
  let p = input.trim();
  if (p === "~") p = home;
  else if (p.startsWith("~/")) p = home + p.slice(1);
  else if (p.startsWith("~")) p = "/Users/" + p.slice(1);
  else if (!p.startsWith("/")) p = join(home, p);
  const out: string[] = [];
  for (const part of p.split("/")) {
    if (part === "" || part === ".") continue;
    if (part === "..") out.pop();
    else out.push(part);
  }
  let s = "/" + out.join("/");
  if (/^\/(var|tmp|etc)(\/|$)/.test(s)) s = "/private" + s;
  if (
    /^\/System\/Volumes\/Data\/(Users|Library|Applications|Volumes|private|opt|cores|usr\/local|System\/Library\/(Caches|Assets|AssetsV2))(\/|$)/.test(
      s,
    )
  )
    s = s.slice("/System/Volumes/Data".length);
  return s;
}

/** The home folder a path is under: yours, or another account's in /Users. */
function homeOf(p: string): string | undefined {
  const home = homedir();
  if (p === home || p.startsWith(home + "/")) return home;
  const m = /^\/Users\/([^/]+)/.exec(p);
  if (m && m[1] !== "Shared" && m[1] !== "Deleted Users") return m[0];
  return undefined;
}

/** ~ for your home folder, so paths read the way the answers write them. */
export function tilde(p: string): string {
  const home = homedir();
  if (p === home) return "~";
  if (p.startsWith(home + "/")) return "~" + p.slice(home.length);
  return p;
}

/** The entry for a path: the rule whose match ends deepest in it; ties go to the more specific rule. */
export function lookup(atlas: Atlas, input: string): Match | undefined {
  const path = normalize(input);
  const home = homeOf(path);
  let best: { c: Compiled; end: number; folder: string } | undefined;
  for (const c of rules(atlas)) {
    if (c.needle && !path.includes(c.needle)) continue;
    if (c.anchor === "~" && !home) continue;
    const re = new RegExp(c.anchor === "~" ? "^" + escapeRe(home as string) + c.source : c.source);
    const m = re.exec(path);
    if (!m) continue;
    let end = m.index + m[0].length;
    if (end > 1 && path[end - 1] === "/") end--;
    const folder = path.slice(0, end);
    if (c.rule.beside && !isFile(join(dirname(folder), c.rule.beside))) continue;
    if (c.rule.has && !isFile(join(folder, c.rule.has))) continue;
    if (!best || end > best.end || (end === best.end && c.weight > best.c.weight)) best = { c, end, folder };
  }
  if (!best) return undefined;
  const verdict = best.c.rule.verdict ?? best.c.folder.verdict;
  return {
    folder: best.c.folder,
    path,
    matched: best.folder,
    inside: best.folder !== path,
    verdict,
    label: LABELS[verdict],
    note: best.c.rule.note,
  };
}

/** Known folders inside a path that isn't one itself, such as ~/Library. */
export function inside(atlas: Atlas, input: string): { folder: Folder; path: string }[] {
  const path = normalize(input);
  const home = homeOf(path);
  const seen = new Set<string>();
  const out: { folder: Folder; path: string }[] = [];
  for (const c of rules(atlas)) {
    if (c.anchor === "*" || seen.has(c.folder.id)) continue;
    if (c.anchor === "~" && !home) continue;
    const full = c.anchor === "~" ? home + c.rule.glob.slice(1) : c.rule.glob;
    if (path === "/" || full.startsWith(path + "/")) {
      seen.add(c.folder.id);
      out.push({ folder: c.folder, path: tilde(full) });
    }
  }
  return out.sort((a, b) => a.path.localeCompare(b.path));
}
