# Is It Safe to Delete?

Check whether a folder on your Mac is safe to delete before you delete it. Each answer has a verdict, a short answer,
whether the folder comes back, how to clear it safely, and the sources behind it, for 93 folders that fill Macs: app
caches, `node_modules`, Xcode's DeviceSupport, Docker.raw, Ollama's models, the Photos library and more.

## Commands

- **Search Mac Folders**: search by name ("docker", "xcode", "npm"), or type a path such as `~/Library/Caches/com.example.app`. A path inside a known folder gets that folder's answer, and the deepest known folder wins. A path that isn't in the Atlas shows the known folders inside it.
- **Check Selected Folder**: select one or more folders or files in Finder, then run it.

## Verdicts

- **Rebuilds**: comes back by itself. Clearing it costs time or a download, not your data.
- **Safe**: logs and leftovers nobody needs.
- **You decide**: yours to judge. It doesn't come back, or only by downloading or making it again.
- **Leave it**: leave it to macOS or the app.

Some folders a page lists only as the place an item lives, such as the Homebrew Cellar or a whole iMovie library, get
their own verdict and the page's warning about them.

## Privacy

Nothing is deleted, and nothing about your files leaves your Mac: paths are matched on your Mac. The extension ships
with the answers and fetches the latest copy of one public file,
[atlas.json](https://github.com/siftmac/mac-folder-atlas/blob/main/atlas.json), from GitHub.

## Data

The answers come from the [Mac Folder Atlas](https://github.com/siftmac/mac-folder-atlas), open data under CC BY 4.0
(“Mac Folder Atlas (siftmac.com)”). Each one links its full answer and its sources. To report a wrong answer or a
missing folder, use the action in the extension or [open an issue](https://github.com/siftmac/mac-folder-atlas/issues).
