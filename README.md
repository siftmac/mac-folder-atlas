# Mac Folder Atlas

**Is it safe to delete this folder on a Mac?** 93 folders and files that fill Macs, from `~/Library/Caches` and
`node_modules` to Docker.raw, Xcode's DeviceSupport and Ollama's models, each with a verdict, a short answer, whether
it comes back, how to clear it safely, and sources. Open data under CC BY 4.0, a command-line tool, and a Raycast
extension.

```console
$ folder-atlas ~/Library/Caches
Rebuilds · Your caches folder (~/Library/Caches)
Yes, app by app, with each app quit. Comes back? Yes. It starts refilling as soon as you use your apps, so
clearing it buys space for a while rather than for good.
https://siftmac.com/safe-to-delete/library-caches

$ folder-atlas /opt/homebrew/Cellar
Leave it · /opt/homebrew/Cellar
Don’t delete folders in the Cellar by hand: Homebrew links each installed version into its `bin` and other
folders. `brew cleanup` removes old versions, and `brew uninstall` a package you don’t need.
See “Homebrew’s cache and old versions”: https://siftmac.com/safe-to-delete/homebrew-cache
```

Browse every folder in **[ATLAS.md](ATLAS.md)**.

## Verdicts

| Verdict | Means | Folders |
|---|---|---|
| **Rebuilds** | Comes back by itself. Clearing it costs time or a download, not your data. | 46 |
| **Safe** | Logs and leftovers nobody needs. | 5 |
| **You decide** | Yours to judge: it doesn't come back, or only by downloading or making it again. | 23 |
| **Leave it** | Leave it to macOS or the app. | 19 |

A verdict is about the folder as a whole. Most answers come with a "but": quit the app first, use the tool's own
clean command, keep the project you're working on. The short answer says it, and the full answer explains it.

## The command: `folder-atlas`

```sh
brew install siftmac/tap/folder-atlas
```

Or take the one file: it's a plain shell script with the answers inside, so there's nothing else to install.

```sh
curl -fsSL https://raw.githubusercontent.com/siftmac/mac-folder-atlas/main/bin/folder-atlas -o folder-atlas
chmod +x folder-atlas   # then move it into a folder on your PATH
```

```console
$ folder-atlas ~/Library/Caches/com.example.app      # inside a known folder
$ folder-atlas node_modules .venv target             # project folders, from inside the project
$ folder-atlas ~/Library/Caches/*                    # one line for each folder in there
  Rebuilds    ~/Library/Caches/Homebrew         Homebrew’s cache and old versions
  Leave it    ~/Library/Caches/com.apple.Music  Your caches folder (~/Library/Caches) (see folder-atlas …)
  Rebuilds    ~/Library/Caches/com.example.app  Your caches folder (~/Library/Caches) (inside it)
$ folder-atlas docker                                # by name
$ folder-atlas ~/Library                             # not a known folder itself: lists the known ones inside
$ folder-atlas -m ~/.npm                             # more: the whole short answer, how to measure and clear it
$ folder-atlas -l                                    # list all 93
$ folder-atlas -o ~/.ollama/models                   # also open the full answer in your browser
$ folder-atlas -j ~/.npm | jq .verdict               # JSON, one object per line
$ find ~/code -name node_modules -prune | folder-atlas -j   # paths on standard input
```

It only reads. It never deletes, moves or measures anything, and it doesn't touch the network: the answers are
inside the script.

**How it matches.** `~` and relative paths work, as do `/var/…`, `/tmp/…` and `/System/Volumes/Data/…`. A path inside
a known folder gets that folder's answer, and the deepest known folder wins: `~/Library/Caches/com.spotify.client/Data`
is Spotify's cache, not just "a cache". Project folders match wherever they are (`node_modules`, `.venv`,
`__pycache__`, `.next`), and the generic names only next to their marker file: `target` beside `Cargo.toml`, `build`
beside `pubspec.yaml`, `.build` beside `Package.swift`, `Pods` beside `Podfile`. Where a page lists a folder only as the
place an item lives, such as the Homebrew Cellar, the iMovie library or `~/Library/Safari`, that folder gets its own
verdict and the page's warning about it.

**Why not `atlas`?** MongoDB's Atlas CLI, Ariga's Atlas and Nim's package cloner already install an `atlas` command
through Homebrew. If you use none of them: `alias atlas=folder-atlas`.

**Requirements:** the `sh` and `awk` every Mac already has. It runs on Linux too, for paths you paste.

## The data

| File | What |
|---|---|
| [`atlas.json`](atlas.json) | Every folder, one record each, with the verdict definitions. The main file. |
| [`atlas.csv`](atlas.csv) | The same, flattened for spreadsheets: id, name, category, verdict, paths, short answer, comes back, link. |
| [`ATLAS.md`](ATLAS.md) | A table to browse, grouped by category. |
| [`schema.json`](schema.json) | JSON Schema for `atlas.json`. |

```sh
curl -s https://raw.githubusercontent.com/siftmac/mac-folder-atlas/main/atlas.json |
  jq -r '.folders[] | select(.verdict == "rebuilds") | .paths[]'
```

A record, shortened:

```json
{
  "id": "npm-cache",
  "name": "npm’s cache (~/.npm)",
  "question": "Is it safe to delete ~/.npm, npm’s cache?",
  "category": "Package caches",
  "paths": ["~/.npm", "~/.npm/_cacache", "~/.npm/_npx"],
  "verdict": "rebuilds",
  "verdict_label": "Rebuilds",
  "answer": "**Yes.** `~/.npm` only holds copies of packages npm has already downloaded, plus logs and tools fetched by `npx`.",
  "summary": ["**Yes.** …", "**What it costs you:** …", "**Does it come back?** Yes. …"],
  "comes_back": "Yes. npm adds to it with every install and never removes anything on its own.",
  "what": "npm keeps a copy of every package tarball and registry answer it fetches, …",
  "measure": ["du -sh ~/.npm\ndu -sh ~/.npm/_cacache ~/.npm/_npx ~/.npm/_logs"],
  "how_to_clear": "1. Let any `npm install` that’s running finish.\n2. For a trim, run `npm cache verify`. …",
  "clear_commands": ["npm cache verify\nnpm cache clean --force", "rm -rf ~/.npm/_npx/*"],
  "sources": [{"title": "npm Docs: npm cache", "url": "https://docs.npmjs.com/cli/v11/commands/npm-cache"}, …],
  "see_also": ["node-modules", "yarn-cache", "pnpm-store", "bun-cache"],
  "match": [{"glob": "~/.npm"}, {"glob": "~/.npm/_cacache"}, {"glob": "~/.npm/_npx"}],
  "url": "https://siftmac.com/safe-to-delete/npm-cache",
  "markdown_url": "https://siftmac.com/safe-to-delete/npm-cache.md",
  "published": "2026-11-21",
  "updated": "2026-11-21"
}
```

- Text fields are Markdown, with links made absolute. `answer` is the first sentence of the summary, or the first two
  when the first is only a word or three ("**Yes.**").
- `paths` are written for people: `~` is the home folder, `<project>` any project folder, `…` any folders in between.
  `match` turns them into globs for tools: `*` is part of one name, `**/` any folders, and a path matches a glob when
  it is that folder or inside it. A match rule can have `beside` (a file that must sit next to the folder), `has` (a
  file that must be inside it), and a `verdict` with a `note` for a folder the page treats differently.
- `url` is the full answer, with what the folder is, how big it gets, how to clear it, what happens afterwards and
  questions people ask. `markdown_url` is the same page as plain Markdown, for AI tools.
- `measure` and `clear_commands` are shell commands as the page gives them. Read the page before running a command
  that deletes.

Ideas for using it: label folders in a disk-space tool, warn before a cleanup script removes something that doesn't
come back, answer "can I delete this?" in a chat bot or an AI assistant, or check a path in CI before a cache step.

## Raycast

[`raycast/`](raycast) holds a Raycast extension, **Is It Safe to Delete?**: search the Atlas by name or path, or check
the folders selected in Finder. It's on its way to the Raycast Store; to try it now,
`cd raycast && npm install && npm run dev`.

## Where the answers come from

Each answer is a page on [siftmac.com/safe-to-delete](https://siftmac.com/safe-to-delete/), written from Apple's and
each tool's own documentation, which every record lists in `sources`. `scripts/sync.py` regenerates this repo from
those pages, so the Atlas changes when a page does; `updated` is the date the page last changed. The pages are written
for [SiftMac](https://siftmac.com), a disk cleaner for Mac that gives the same verdicts in its space map.

**Wrong answer, or a folder that's missing?** [Open an issue](https://github.com/siftmac/mac-folder-atlas/issues)
with the path and what you found. Answers are fixed at the source page, then synced here, so please don't edit
`atlas.json` by hand. Pull requests for the command and the extension are welcome; run `sh test/test.sh` first.

## Credit and licences

- **The answers** (`atlas.json`, `atlas.csv`, `ATLAS.md`, and the copies inside `bin/folder-atlas` and
  `raycast/src/atlas.json`) are licensed under [CC BY 4.0](LICENSE-DATA). Credit them as **“Mac Folder Atlas
  (siftmac.com)”** and, where you show one entry, link its `url`.
- **The code** (the command, the scripts, the tests and the Raycast extension) is under the [MIT licence](LICENSE).
