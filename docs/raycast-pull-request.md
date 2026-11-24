<!--
Draft text for the raycast/extensions pull request that adds raycast/ to the Raycast Store.

Before publishing:
1. Install Raycast and sign in. Set "author" in package.json to your Raycast username: "siftmac" is free on Raycast
   (checked 24 Nov 2026), which keeps the brand off your personal name.
2. cd raycast && npm install && npm run dev: try both commands, then npm run build and npm run lint (all must pass).
3. Take 3 screenshots with Raycast's own Window Capture command (2000 × 1250 PNG) into raycast/metadata/:
   is-it-safe-to-delete-1.png (Search Mac Folders, ~/Library/Caches selected), -2.png (a path typed:
   /opt/homebrew/Cellar), -3.png (Check Selected Folder on a node_modules folder). Then record a short screencast for
   the PR below.
4. npm run publish: it forks raycast/extensions, commits the extension and opens the PR; paste the text below into it.
-->

## Description

Adds **Is It Safe to Delete?**, which tells you whether a folder on your Mac is safe to delete, from the open
[Mac Folder Atlas](https://github.com/siftmac/mac-folder-atlas) (CC BY 4.0): 93 folders that fill Macs, each with a
verdict (Rebuilds, Safe, You decide, Leave it), a short answer, whether it comes back, how to clear it safely and its
sources.

Two commands:

- **Search Mac Folders**: search by name, or type a path. A path inside a known folder gets that folder's answer (the
  deepest known folder wins), generic project folders only match beside their marker file (`target` next to
  `Cargo.toml`, `build` next to `pubspec.yaml`), and a path that isn't in the Atlas lists the known folders inside it.
- **Check Selected Folder**: answers for the items selected in Finder, via `getSelectedFinderItems`.

The detail pane shows the answer, where the folder is, how to measure it and how to clear it, with actions to open the
full answer, show the folder in Finder, and copy the path or the command from the answer.

Notes for review:

- Nothing is deleted or moved, and no file paths leave the Mac: matching runs locally.
- The extension ships with the data (`src/atlas.json`) and refreshes it with `useFetch` from the repo's raw
  `atlas.json` on GitHub, keeping the bundled copy when offline. `src/atlas.json` is generated, so it's in
  `.prettierignore`.
- No API keys, accounts or preferences.

## Screencast

<!-- Add the screencast here: search "xcode", type ~/Library/Caches/com.apple.Music, then Check Selected Folder on a
node_modules folder. -->

## Checklist

- [x] I read the [extension guidelines](https://developers.raycast.com/basics/prepare-an-extension-for-store)
- [x] I read the [documentation about publishing](https://developers.raycast.com/basics/publish-an-extension)
- [ ] I ran `npm run build` and [tested this distribution build in Raycast](https://developers.raycast.com/basics/prepare-an-extension-for-store#metadata-and-configuration)
- [x] I checked that files in the `assets` folder are used by the extension itself
- [x] I checked that assets used in the `README` are located outside the metadata folder if they were not generated with our [metadata tool](https://developers.raycast.com/basics/prepare-an-extension-for-store#how-to-use-it)
