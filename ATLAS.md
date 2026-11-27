# The Mac Folder Atlas

142 folders and files that fill Macs, each with a verdict, a short answer and a link to the full answer: what it is, how big it gets, how to clear it safely and what happens afterwards.

| Verdict | Means | Folders |
|---|---|---|
| **Rebuilds** | Comes back by itself. Clearing it costs time or a download, not your data. | 64 |
| **Safe** | Logs and leftovers nobody needs. | 5 |
| **You decide** | Yours to judge: it doesn't come back, or only by downloading or making it again. | 44 |
| **Leave it** | Leave it to macOS or the app. | 29 |

Made from [`atlas.json`](atlas.json) by `scripts/sync.py`. To fix an answer, open an issue; this file is regenerated, not edited.

**Categories:** [Library and system](#library-and-system) · [macOS files](#macos-files) · [Apple apps](#apple-apps) · [Apps](#apps) · [Browsers](#browsers) · [Creative apps](#creative-apps) · [Games](#games) · [Developer tools](#developer-tools) · [Project folders](#project-folders) · [Package caches](#package-caches) · [AI tools](#ai-tools) · [Virtual machines](#virtual-machines)

## Library and system

| Folder | Where | Verdict | Short answer |
|---|---|---|---|
| [App data (Application Support)](https://siftmac.com/safe-to-delete/application-support) | `~/Library/Application Support`<br>`/Library/Application Support` | Leave it | **No, not as a whole.** |
| [Application Scripts folder](https://siftmac.com/safe-to-delete/application-scripts) | `~/Library/Application Scripts` | Leave it | **No point.** The folder holds hundreds of subfolders, but almost all of them are empty. |
| [Biome folder](https://siftmac.com/safe-to-delete/biome) | `~/Library/Biome` | Leave it | **Leave it.** Biome is the store macOS uses to build suggestions from how you use your Mac. |
| [Core Spotlight index](https://siftmac.com/safe-to-delete/core-spotlight-metadata) | `~/Library/Metadata/CoreSpotlight` | Leave it | **No.** This folder is the index that lets Spotlight find things inside your apps, such as a message in Mail or a line in Notes. |
| [Crash reports (DiagnosticReports)](https://siftmac.com/safe-to-delete/diagnostic-reports) | `~/Library/Logs/DiagnosticReports`<br>`/Library/Logs/DiagnosticReports` | Safe | **Yes.** Every file in it is a report macOS wrote after something crashed, hung or ran into trouble. |
| [Document versions (.DocumentRevisions-V100)](https://siftmac.com/safe-to-delete/document-revisions) | `/System/Volumes/Data/.DocumentRevisions-V100` | Leave it | **Leave the folder itself.** |
| [File change logs (.fseventsd)](https://siftmac.com/safe-to-delete/fseventsd) | `/System/Volumes/Data/.fseventsd`<br>`/Volumes/<drive>/.fseventsd` | Leave it | **No, leave it.** `.fseventsd` is macOS’s running record of which folders changed on a disk. |
| [Log files (~/Library/Logs)](https://siftmac.com/safe-to-delete/library-logs) | `~/Library/Logs`<br>`/Library/Logs` | Safe | **Yes, your old ones.** |
| [macOS downloads (AssetsV2)](https://siftmac.com/safe-to-delete/assetsv2) | `/System/Library/AssetsV2` | Leave it | **No.** AssetsV2 is where macOS keeps parts it downloads after it’s installed: Apple Intelligence and Siri models, voices, dictionaries, fonts, security data and software updates on their way in. |
| [Removed accounts (Deleted Users)](https://siftmac.com/safe-to-delete/deleted-users) | `/Users/Deleted Users` | You decide | **Yes, once you’ve checked it.** |
| [Sandboxed apps’ data (Containers)](https://siftmac.com/safe-to-delete/containers) | `~/Library/Containers` | Leave it | **No, not the folder, and not the container of an app you use.** |
| [Saved windows (Saved Application State)](https://siftmac.com/safe-to-delete/saved-application-state) | `~/Library/Saved Application State` | Safe | **Yes.** It only remembers which windows each app had open, and where, so they reappear when you reopen the app or restart the Mac. |
| [Settings files (.plist in Preferences)](https://siftmac.com/safe-to-delete/preferences-plist-files) | `~/Library/Preferences`<br>`/Library/Preferences` | Leave it | **Not all of them.** |
| [Shared app data (Group Containers)](https://siftmac.com/safe-to-delete/group-containers) | `~/Library/Group Containers` | Leave it | **No.** Each folder here holds data that several apps from one developer share, or that an app shares with its widgets and extensions. |
| [Software Update’s folder](https://siftmac.com/safe-to-delete/library-updates) | `/Library/Updates` | Leave it | **No.** `/Library/Updates` belongs to Software Update. |
| [Swap files (swapfile)](https://siftmac.com/safe-to-delete/swap-files) | `/System/Volumes/VM`<br>`/private/var/vm` | Leave it | **No.** Swap files hold parts of memory macOS moved to the disk to make room. |
| [System logs (/var/log)](https://siftmac.com/safe-to-delete/private-var-log) | `/private/var/log`<br>`/var/log` | Leave it | **No need.** `/private/var/log` belongs to macOS, which rotates and compresses these logs by itself. |
| [System-wide caches (/Library/Caches)](https://siftmac.com/safe-to-delete/system-library-caches) | `/Library/Caches`<br>`/System/Library/Caches` | Leave it | **No, leave it to macOS.** |
| [Temporary files (/private/var/folders)](https://siftmac.com/safe-to-delete/var-folders) | `/private/var/folders` | Leave it | **No, not by hand.** |
| [Temporary folders (/tmp)](https://siftmac.com/safe-to-delete/private-tmp) | `/private/tmp`<br>`/private/var/tmp` | Leave it | **Leave them.** The folders themselves must exist, and what’s inside often belongs to something that is running right now. |
| [The dyld shared cache](https://siftmac.com/safe-to-delete/dyld-cache) | `/System/Volumes/Preboot/Cryptexes/OS/System/Library/dyld`<br>`/System/Library/dyld`<br>`/private/var/db/dyld` | Leave it | **No.** The dyld shared cache is where macOS keeps all of its system libraries, the code every app on your Mac runs on. |
| [The sleep image (sleepimage)](https://siftmac.com/safe-to-delete/sleepimage) | `/private/var/vm/sleepimage` | Leave it | **No, leave it.** It’s where macOS saves a copy of memory so a sleeping Mac can pick up where it was, even if the battery runs out. |
| [The Spotlight index (.Spotlight-V100)](https://siftmac.com/safe-to-delete/spotlight-index) | `/System/Volumes/Data/.Spotlight-V100`<br>`/Volumes/<drive>/.Spotlight-V100` | Leave it | **Not by hand.** `.Spotlight-V100` is one disk’s search index, the thing Spotlight, Finder’s search, Mail’s search and many apps look things up in. |
| [Unified log store](https://siftmac.com/safe-to-delete/diagnostics-and-uuidtext) | `/private/var/db/diagnostics`<br>`/private/var/db/uuidtext` | Leave it | **No.** These two folders are the unified log, the record that Console and the `log` command read. |
| [Your caches folder (~/Library/Caches)](https://siftmac.com/safe-to-delete/library-caches) | `~/Library/Caches` | Rebuilds | **Yes**, app by app, with each app quit. |

## macOS files

| Folder | Where | Verdict | Short answer |
|---|---|---|---|
| [._ files (AppleDouble) and dot_clean](https://siftmac.com/safe-to-delete/dot-underscore-files) | `/Volumes/MyDrive/._*`<br>`__MACOSX/` | Safe | **Yes**, on a drive that goes into a TV, car stereo, camera or Windows PC. |
| [.DS_Store files](https://siftmac.com/safe-to-delete/ds-store-files) | `~/Desktop/.DS_Store`<br>`~/Documents/.DS_Store`<br>`/Volumes/MyDrive/.DS_Store` | Rebuilds | **Yes.** A `.DS_Store` file only remembers how Finder shows its folder: the view, where icons sit and similar settings. |
| [.Trashes and Recovered Files](https://siftmac.com/safe-to-delete/dot-trashes) | `/Volumes/<drive>/.Trashes`<br>`/Volumes/<drive>/.TemporaryItems`<br>`~/.Trash/Recovered Files` | You decide | **Yes, by emptying the Trash.** |
| [Aerial wallpaper videos](https://siftmac.com/safe-to-delete/aerial-wallpapers) | `/Library/Application Support/com.apple.idleassetsd` | Rebuilds | **Yes, the videos.** The aerial clips in `/Library/Application Support/com.apple.idleassetsd/Customer` are downloads, not part of macOS. |
| [Content Caching data](https://siftmac.com/safe-to-delete/content-caching) | `/Library/Application Support/Apple/AssetCache`<br>`/Library/Application Support/Apple/AssetCache/Data` | Rebuilds | **Yes, with the Reset button.** |
| [Downloaded voices](https://siftmac.com/safe-to-delete/siri-voices) | `/System/Library/AssetsV2/com_apple_MobileAsset_MacinTalkVoiceAssets`<br>`/System/Library/AssetsV2/com_apple_MobileAsset_VoiceServices_CombinedVocalizerVoices` | You decide | **Yes, in System Settings.** |
| [Font caches](https://siftmac.com/safe-to-delete/font-caches) | `/private/var/folders/…/C/com.apple.FontRegistry` | Rebuilds | **Yes**, with Apple’s tools. |
| [iPhone and iPad update files (.ipsw)](https://siftmac.com/safe-to-delete/iphone-software-updates) | `~/Library/iTunes/iPhone Software Updates`<br>`~/Library/iTunes/iPad Software Updates`<br>`~/Library/iTunes/iPod Software Updates` | Rebuilds | **Yes.** An `.ipsw` file is a copy of iOS or iPadOS your Mac downloaded to update or restore a device. |
| [Keychains folder](https://siftmac.com/safe-to-delete/keychains) | `~/Library/Keychains`<br>`~/Library/Keychains/login.keychain-db` | Leave it | **No.** `~/Library/Keychains` holds your login keychain and this Mac’s copy of your iCloud Keychain or Local Items: saved passwords, passkeys, certificates and private keys. |
| [lost+found folder](https://siftmac.com/safe-to-delete/lost-and-found) | `/lost+found`<br>`/Volumes/<drive>/lost+found` | You decide | **Yes, after checking it.** |
| [Old macOS installers](https://siftmac.com/safe-to-delete/macos-installers) | `/Applications/Install macOS Tahoe.app`<br>`/Applications/Install macOS Sequoia.app`<br>`~/Applications/Install macOS Sonoma.app` | Rebuilds | **Yes, the installers.** An app named “Install macOS …” in Applications is a full macOS installer that was downloaded and never removed. |
| [Quick Look’s thumbnail cache](https://siftmac.com/safe-to-delete/quicklook-thumbnail-cache) | `/private/var/folders/…/C/com.apple.quicklook.ThumbnailsAgent/com.apple.QuickLook.thumbnailcache`<br>`/private/var/folders/…/C/com.apple.QuickLook.thumbnailcache` | Rebuilds | **Yes.** It holds the little previews Finder shows instead of plain icons for photos, PDFs, videos and documents. |
| [Relocated Items folder](https://siftmac.com/safe-to-delete/relocated-items) | `/Users/Shared/Relocated Items`<br>`~/Desktop/Relocated Items` | You decide | **Usually yes,** once you’ve looked inside. |
| [The Downloads folder](https://siftmac.com/safe-to-delete/downloads-folder) | `~/Downloads` | You decide | **Yes, whatever you no longer need.** |
| [The Preboot volume](https://siftmac.com/safe-to-delete/preboot-volume) | `/System/Volumes/Preboot` | Leave it | **No.** Preboot is one of the volumes macOS starts up from. |
| [The Trash](https://siftmac.com/safe-to-delete/trash) | `~/.Trash` | You decide | **Yes, once you’ve looked through it.** |

## Apple apps

| Folder | Where | Verdict | Short answer |
|---|---|---|---|
| [App Store cache](https://siftmac.com/safe-to-delete/app-store-cache) | `~/Library/Caches/com.apple.appstoreagent`<br>`~/Library/Caches/com.apple.appstorecomponentsd`<br>`/private/var/folders/…/C/com.apple.AppStore` | Rebuilds | **Yes, but it rarely helps.** |
| [Apple Music downloads](https://siftmac.com/safe-to-delete/apple-music-downloads) | `~/Music/Music/Media` | You decide | **Yes, with Remove Download.** |
| [Apple TV app downloads](https://siftmac.com/safe-to-delete/tv-app-downloads) | `~/Movies/TV`<br>`~/Movies/TV/Media` | You decide | **Yes, from inside the TV app.** |
| [Downloaded podcast episodes](https://siftmac.com/safe-to-delete/podcasts-downloads) | `~/Library/Group Containers/243LU875E5.groups.com.apple.podcasts/Library/Cache` | You decide | **Yes.** A downloaded episode is a copy for listening offline. |
| [GarageBand and Logic sound library](https://siftmac.com/safe-to-delete/garageband-logic-sound-library) | `~/Music/Logic Pro Library.bundle`<br>`/Library/Application Support/GarageBand`<br>`/Library/Application Support/Logic`<br>`/Library/Audio/Apple Loops/Apple` | You decide | **Yes, if you don’t make music on this Mac.** |
| [iCloud Drive’s local copies](https://siftmac.com/safe-to-delete/icloud-drive-local-files) | `~/Library/Mobile Documents/com~apple~CloudDocs`<br>`~/Library/Mobile Documents` | You decide | **Only with Remove Download.** |
| [iMovie render files](https://siftmac.com/safe-to-delete/imovie-render-files) | `~/Movies/iMovie Library.imovielibrary` | Rebuilds | **Yes, with iMovie’s own Delete button.** |
| [Mail Downloads](https://siftmac.com/safe-to-delete/mail-downloads) | `~/Library/Containers/com.apple.mail/Data/Library/Mail Downloads` | Safe | **Yes, for attachments you only opened.** |
| [Mail’s data folder](https://siftmac.com/safe-to-delete/mail-data) | `~/Library/Mail`<br>`~/Library/Mail/V10` | Leave it | **No.** `~/Library/Mail` is Mail’s copy of your email: every mailbox, message and downloaded attachment, including mailboxes kept On My Mac and POP mail that may exist nowhere else. |
| [Messages attachments](https://siftmac.com/safe-to-delete/messages-attachments) | `~/Library/Messages/Attachments` | You decide | **Yes, if you can live without them**, and if you delete them in Messages or Storage settings rather than in the folder. |
| [Photo Booth Library](https://siftmac.com/safe-to-delete/photo-booth-library) | `~/Pictures/Photo Booth Library` | You decide | **Yes, if you don’t want the pictures.** |
| [The Photos library](https://siftmac.com/safe-to-delete/photos-library) | `~/Pictures/Photos Library.photoslibrary` | You decide | **No, not the library itself.** |

## Apps

| Folder | Where | Verdict | Short answer |
|---|---|---|---|
| [Discord’s cache](https://siftmac.com/safe-to-delete/discord-cache) | `~/Library/Application Support/discord/Cache`<br>`~/Library/Application Support/discord/Code Cache`<br>`~/Library/Application Support/discord/GPUCache` | Rebuilds | **Yes**, with Discord fully quit. |
| [Dropbox’s cache folder](https://siftmac.com/safe-to-delete/dropbox-cache) | `~/Dropbox/.dropbox.cache`<br>`~/Library/Group Containers/<ID>.com.getdropbox.dropbox.sync/root-mount` | Rebuilds | **Yes**, with Dropbox quit. |
| [Google Drive’s cache (DriveFS)](https://siftmac.com/safe-to-delete/google-drive-cache) | `~/Library/Application Support/Google/DriveFS`<br>`~/Library/CloudStorage` | Leave it | **Leave it.** `DriveFS` is Google Drive for desktop’s cache, and Google’s admin documentation says files are moved there before they’re uploaded. |
| [Microsoft Teams’ cache](https://siftmac.com/safe-to-delete/microsoft-teams-cache) | `~/Library/Containers/com.microsoft.teams2`<br>`~/Library/Group Containers/UBF8T346G9.com.microsoft.teams`<br>`~/Library/Application Support/Microsoft/Teams` | Rebuilds | **Yes**, with Teams quit. |
| [Slack’s cache](https://siftmac.com/safe-to-delete/slack-cache) | `~/Library/Application Support/Slack`<br>`~/Library/Containers/com.tinyspeck.slackmacgap/Data/Library/Application Support/Slack`<br>`~/Library/Caches/com.tinyspeck.slackmacgap` | Rebuilds | **Yes.** Your messages, files and channels are kept in your Slack workspaces; the Mac app stores copies so it opens quickly. |
| [Spotify’s cache and downloads](https://siftmac.com/safe-to-delete/spotify-cache) | `~/Library/Caches/com.spotify.client`<br>`~/Library/Application Support/Spotify` | Rebuilds | **Yes, the cache.** It’s parts of songs and podcasts Spotify saved so they play without stalling, and **Clear cache** in Spotify’s settings removes it safely. |
| [Telegram’s media cache](https://siftmac.com/safe-to-delete/telegram-cache) | `~/Library/Group Containers/6N38VWS5BX.ru.keepcoder.Telegram`<br>`~/Library/Application Support/Telegram Desktop` | Rebuilds | **Yes.** Telegram stores your chats and media in its cloud, and what’s on your Mac is a cache. |
| [WhatsApp’s media and data](https://siftmac.com/safe-to-delete/whatsapp-media) | `~/Library/Group Containers/group.net.whatsapp.WhatsApp.shared` | You decide | **Be careful.** WhatsApp for Mac holds a copy of your recent chats and the photos, videos and files in them. |
| [Zoom recordings and cache](https://siftmac.com/safe-to-delete/zoom-recordings) | `~/Documents/Zoom`<br>`~/Library/Application Support/zoom.us/data` | You decide | **Your call.** A computer recording is a video Zoom made on this Mac, and it may be the only copy: Zoom’s help notes it can only be played on the device where it was made. |

## Browsers

| Folder | Where | Verdict | Short answer |
|---|---|---|---|
| [Chrome’s code_sign_clone](https://siftmac.com/safe-to-delete/chrome-code-sign-clone) | `/private/var/folders/…/X/com.google.Chrome.code_sign_clone` | Rebuilds | **Mostly, but let Chrome do it.** |
| [Chrome’s on-device AI model](https://siftmac.com/safe-to-delete/chrome-on-device-ai-model) | `~/Library/Application Support/Google/Chrome/OptGuideOnDeviceModel` | Leave it | **Not by hand.** The folder holds Gemini Nano, the AI model Chrome keeps on your Mac for features like help with writing and scam warnings. |
| [Firefox’s cache](https://siftmac.com/safe-to-delete/firefox-cache) | `~/Library/Caches/Firefox/Profiles` | Rebuilds | **Yes.** Mozilla’s own documentation says this folder is for caches that can safely be deleted. |
| [Google Chrome’s cache](https://siftmac.com/safe-to-delete/chrome-cache) | `~/Library/Caches/Google/Chrome/Default/Cache`<br>`~/Library/Caches/Google/Chrome/Default/Code Cache` | Rebuilds | **Yes.** Chrome’s cache is parts of pages it saved so sites open faster. |
| [Safari’s cache and website data](https://siftmac.com/safe-to-delete/safari-cache) | `~/Library/Caches/com.apple.Safari`<br>`~/Library/Containers/com.apple.Safari`<br>`~/Library/Safari` | Rebuilds | **Yes.** The cache is copies of pages, images and scripts Safari saved so sites open faster, and Safari fetches them again as you browse. |

## Creative apps

| Folder | Where | Verdict | Short answer |
|---|---|---|---|
| [Adobe’s media cache](https://siftmac.com/safe-to-delete/adobe-media-cache) | `~/Library/Application Support/Adobe/Common/Media Cache Files`<br>`~/Library/Application Support/Adobe/Common/Media Cache` | Rebuilds | **Yes.** The media cache is audio and video that Premiere, After Effects and Media Encoder processed so previews play smoothly, and Adobe says deleted cache files are recreated automatically when your media needs them. |
| [After Effects’ disk cache](https://siftmac.com/safe-to-delete/after-effects-disk-cache) | `~/Library/Caches/Adobe/After Effects` | Rebuilds | **Yes.** The disk cache is frames After Effects already rendered, kept so previews don’t render them again. |
| [DaVinci Resolve’s render cache](https://siftmac.com/safe-to-delete/davinci-resolve-cache) | `~/Movies/CacheClip` | Rebuilds | **Yes.** CacheClip holds render cache: clips, effects and grades Resolve already rendered so playback stays smooth. |
| [Final Cut Pro’s render files](https://siftmac.com/safe-to-delete/final-cut-pro-render-files) | `~/Movies/<library name>.fcpbundle` | Rebuilds | **Yes**, from inside Final Cut Pro. |
| [Lightroom Classic’s previews](https://siftmac.com/safe-to-delete/lightroom-previews) | `~/Pictures/Lightroom/Lightroom Catalog Previews.lrdata` | Rebuilds | **Yes**, with Lightroom Classic quit. |

## Games

| Folder | Where | Verdict | Short answer |
|---|---|---|---|
| [Steam games and the Steam folder](https://siftmac.com/safe-to-delete/steam-games) | `~/Library/Application Support/Steam/steamapps`<br>`~/Library/Application Support/Steam/userdata` | You decide | **Mostly.** A game you bought stays in your Steam library and can be installed again. |

## Developer tools

| Folder | Where | Verdict | Short answer |
|---|---|---|---|
| [A project’s .git folder](https://siftmac.com/safe-to-delete/git-folder) | `<project>/.git` | You decide | **Usually not.** `.git` is the repository itself: every commit, branch, tag and stash of the project. |
| [Android emulators (AVDs)](https://siftmac.com/safe-to-delete/android-emulators) | `~/.android/avd` | You decide | **Yes, the ones you don’t use**, from Android Studio’s Device Manager. |
| [Colima, Lima and OrbStack data](https://siftmac.com/safe-to-delete/colima-lima-orbstack) | `~/.colima`<br>`~/.lima`<br>`~/Library/Group Containers/HUAQ24HBR6.dev.orbstack`<br>`~/.orbstack` | You decide | **Only on purpose.** These folders are virtual machines. |
| [Continue and aider files](https://siftmac.com/safe-to-delete/continue-and-aider) | `~/.continue`<br>`~/.continue/index`<br>`~/.continue/sessions`<br>`.aider.chat.history.md`<br>`.aider.input.history`<br>`.aider.tags.cache.v4` | You decide | **Partly.** The index in `~/.continue/index` and aider’s `.aider.tags.cache` folders are derived from your code and get built again. |
| [Cursor’s extensions (~/.cursor)](https://siftmac.com/safe-to-delete/cursor-extensions) | `~/.cursor`<br>`~/.cursor/extensions` | Leave it | **No, not by hand.** |
| [Cursor’s update cache (ShipIt)](https://siftmac.com/safe-to-delete/cursor-update-cache) | `~/Library/Caches/com.todesktop.230313mzl4w4u92.ShipIt` | Rebuilds | **Yes**, with Cursor quit. |
| [Cypress binary cache](https://siftmac.com/safe-to-delete/cypress-cache) | `~/Library/Caches/Cypress` | Rebuilds | **Yes.** It’s Cypress’s binary cache: the Cypress app itself, one folder for each version a project of yours has installed. |
| [Docker Desktop’s Docker.raw](https://siftmac.com/safe-to-delete/docker-raw) | `~/Library/Containers/com.docker.docker/Data/vms/0/data/Docker.raw` | You decide | **No, not as a way to free space.** |
| [Docker’s ~/.docker config folder](https://siftmac.com/safe-to-delete/docker-config-folder) | `~/.docker`<br>`~/.docker/config.json`<br>`~/.docker/contexts`<br>`~/.docker/cli-plugins`<br>`~/.docker/buildx` | Leave it | **No, while you use Docker.** |
| [Electron download caches](https://siftmac.com/safe-to-delete/electron-cache) | `~/Library/Caches/electron`<br>`~/Library/Caches/electron-builder` | Rebuilds | **Yes.** These two folders are download caches for people who build Electron apps. |
| [JetBrains IDE caches](https://siftmac.com/safe-to-delete/jetbrains-caches) | `~/Library/Caches/JetBrains`<br>`~/Library/Logs/JetBrains` | Rebuilds | **Yes**, with the IDE quit. |
| [minikube and kubectl’s cache](https://siftmac.com/safe-to-delete/minikube-and-kube-cache) | `~/.minikube`<br>`~/.kube/cache` | You decide | **Yes, with minikube’s own command**, if you no longer need the local clusters. |
| [Playwright’s browsers](https://siftmac.com/safe-to-delete/playwright-browsers) | `~/Library/Caches/ms-playwright` | Rebuilds | **Yes.** The folder holds browser builds that Playwright downloaded for testing. |
| [Puppeteer’s Chrome downloads](https://siftmac.com/safe-to-delete/puppeteer-cache) | `~/.cache/puppeteer` | Rebuilds | **Yes.** The folder contains copies of Chrome for Testing and `chrome-headless-shell` that Puppeteer fetched. |
| [pyenv’s Python versions](https://siftmac.com/safe-to-delete/pyenv-versions) | `~/.pyenv/versions` | You decide | **One by one**, yes. |
| [Ruby gems and rbenv versions](https://siftmac.com/safe-to-delete/ruby-gems-and-rbenv) | `~/.gem`<br>`~/.rbenv/versions` | You decide | **Not wholesale.** Old versions of gems can go with `gem cleanup`, and a Ruby you’ve stopped using can be removed from `~/.rbenv/versions`. |
| [rustup’s toolchains](https://siftmac.com/safe-to-delete/rustup-toolchains) | `~/.rustup/toolchains` | You decide | **Partly.** Remove the toolchains you don’t build with, using `rustup toolchain uninstall`. |
| [The Android SDK](https://siftmac.com/safe-to-delete/android-sdk) | `~/Library/Android/sdk` | Leave it | **No, not all of it** while you build Android apps: Android Studio, Gradle and the emulator all run from it. |
| [VS Code’s caches and extensions](https://siftmac.com/safe-to-delete/vs-code-cache) | `~/Library/Application Support/Code/Cache`<br>`~/Library/Application Support/Code/CachedData`<br>`~/Library/Application Support/Code/CachedExtensionVSIXs` | Rebuilds | **Yes, the caches**, with VS Code quit. |
| [VS Code’s extensions folder](https://siftmac.com/safe-to-delete/vscode-extensions) | `~/.vscode/extensions` | Leave it | **No, let VS Code do it.** |
| [Windsurf and ~/.codeium](https://siftmac.com/safe-to-delete/windsurf-and-codeium) | `~/.codeium`<br>`~/.codeium/windsurf`<br>`~/Library/Application Support/Windsurf`<br>`~/.windsurf/extensions` | You decide | **Not ~/.codeium.** It is still in use: your MCP server list, user settings, global workflows and skills live there, and the editor’s command-line tools too. |
| [Xcode Archives](https://siftmac.com/safe-to-delete/xcode-archives) | `~/Library/Developer/Xcode/Archives` | You decide | **Partly.** Archives of builds nobody runs any more can go. |
| [Xcode iOS DeviceSupport](https://siftmac.com/safe-to-delete/ios-device-support) | `~/Library/Developer/Xcode/iOS DeviceSupport` | Rebuilds | **Yes**, with Xcode quit, and especially the folders for iOS versions none of your devices run any more. |
| [Xcode simulators (CoreSimulator)](https://siftmac.com/safe-to-delete/xcode-simulators) | `~/Library/Developer/CoreSimulator/Devices`<br>`~/Library/Developer/CoreSimulator/Caches`<br>`~/Library/Developer/Xcode/UserData/Previews` | Rebuilds | **Yes, with Xcode’s own tools.** |

## Project folders

| Folder | Where | Verdict | Short answer |
|---|---|---|---|
| [.turbo and .parcel-cache](https://siftmac.com/safe-to-delete/turbo-and-parcel-cache) | `<project>/.turbo`<br>`<project>/.parcel-cache` | Rebuilds | **Yes.** Both folders store results of earlier builds so the next one can skip work. |
| [__pycache__ folders](https://siftmac.com/safe-to-delete/pycache) | `<project>/**/__pycache__` | Rebuilds | **Yes.** Every file in `__pycache__` is compiled from a `.py` file beside it, and Python compiles it again by itself. |
| [A project’s Pods folder](https://siftmac.com/safe-to-delete/cocoapods-pods-folder) | `<project>/Pods` | Rebuilds | **Yes**, if the project has its `Podfile` and `Podfile.lock`. |
| [Flutter’s build and .dart_tool](https://siftmac.com/safe-to-delete/dart-tool-and-flutter-build) | `<project>/build`<br>`<project>/.dart_tool` | Rebuilds | **Yes.** Flutter has a command for exactly this: `flutter clean` deletes the `build/` and `.dart_tool/` directories. |
| [Next.js .next folders](https://siftmac.com/safe-to-delete/nextjs-cache) | `<project>/.next`<br>`<project>/.next/cache` | Rebuilds | **Yes**, with the dev server stopped. |
| [node_modules folders](https://siftmac.com/safe-to-delete/node-modules) | `<project>/node_modules` | Rebuilds | **Yes**, in projects you aren’t running right now. |
| [pytest, mypy, ruff and tox caches](https://siftmac.com/safe-to-delete/pytest-mypy-tox-caches) | `<project>/.pytest_cache`<br>`<project>/.mypy_cache`<br>`<project>/.ruff_cache`<br>`<project>/.tox` | Rebuilds | **Yes.** All four are written by tools as they run, and each tool makes its folder again the next time you use it. |
| [Python virtual environments](https://siftmac.com/safe-to-delete/python-venv) | `<project>/.venv`<br>`<project>/venv` | Rebuilds | **Yes**, if the project lists its packages. |
| [Rust target folders](https://siftmac.com/safe-to-delete/rust-target-folder) | `<project>/target` | Rebuilds | **Yes.** `target` is everything Cargo compiled for the project, and none of it is source. |
| [Terraform’s .terraform folders](https://siftmac.com/safe-to-delete/terraform-folders) | `<project>/.terraform`<br>`~/.terraform.d/plugin-cache` | Rebuilds | **Yes.** `.terraform` is Terraform’s working folder for cached provider plugins and modules, and `terraform init` builds it again. |
| [Unity’s Library folder](https://siftmac.com/safe-to-delete/unity-library-folder) | `<Unity project>/Library`<br>`<Unity project>/Temp` | Rebuilds | **Yes**, with the project closed. |

## Package caches

| Folder | Where | Verdict | Short answer |
|---|---|---|---|
| [Bun’s cache (~/.bun)](https://siftmac.com/safe-to-delete/bun-cache) | `~/.bun/install/cache` | Rebuilds | **Yes, the cache part.** |
| [Cargo’s registry and git cache](https://siftmac.com/safe-to-delete/cargo-registry) | `~/.cargo/registry`<br>`~/.cargo/git` | Rebuilds | **Yes**, those two. They’re Cargo’s cache of crates and git dependencies, which Cargo extracts or downloads again. |
| [CocoaPods’ cache and Pods](https://siftmac.com/safe-to-delete/cocoapods-cache) | `~/Library/Caches/CocoaPods`<br>`~/.cocoapods/repos` | Rebuilds | **Yes**, all three come back with `pod install`. |
| [conda’s pkgs and environments](https://siftmac.com/safe-to-delete/conda-packages) | `~/miniconda3/pkgs`<br>`/opt/miniconda3/pkgs`<br>`~/miniconda3/envs` | Rebuilds | **Yes, through conda.** `conda clean --all` removes cached packages no environment uses, along with tarballs, index caches and logs. |
| [Dart and Flutter’s pub cache](https://siftmac.com/safe-to-delete/flutter-pub-cache) | `~/.pub-cache` | Rebuilds | **Yes.** It’s pub’s system cache of packages downloaded for your Dart and Flutter projects. |
| [Go’s module and build caches](https://siftmac.com/safe-to-delete/go-module-cache) | `~/go/pkg/mod`<br>`~/Library/Caches/go-build` | Rebuilds | **Yes**, with Go’s own commands. |
| [Gradle’s caches (~/.gradle)](https://siftmac.com/safe-to-delete/gradle-caches) | `~/.gradle/caches`<br>`~/.gradle/wrapper/dists`<br>`~/.gradle/jdks`<br>`~/.gradle/daemon` | Rebuilds | **Yes**, with Gradle stopped. |
| [Homebrew’s cache and old versions](https://siftmac.com/safe-to-delete/homebrew-cache) | `~/Library/Caches/Homebrew`<br>`/opt/homebrew/Cellar`<br>`/usr/local/Cellar` | Rebuilds | **Yes.** It holds bottles and installers Homebrew already downloaded; what you’ve installed runs from elsewhere. |
| [Maven’s local repository (~/.m2)](https://siftmac.com/safe-to-delete/maven-repository) | `~/.m2/repository`<br>`~/.m2/wrapper` | Rebuilds | **Mostly.** Nearly everything in it is libraries and plugins Maven downloaded, and those come back on the next build. |
| [npm’s cache (~/.npm)](https://siftmac.com/safe-to-delete/npm-cache) | `~/.npm`<br>`~/.npm/_cacache`<br>`~/.npm/_npx` | Rebuilds | **Yes.** `~/.npm` only holds copies of packages npm has already downloaded, plus logs and tools fetched by `npx`. |
| [pip’s cache](https://siftmac.com/safe-to-delete/pip-cache) | `~/Library/Caches/pip` | Rebuilds | **Yes.** It’s pip’s download cache plus wheels it built, kept so the next install is faster. |
| [pnpm’s store](https://siftmac.com/safe-to-delete/pnpm-store) | `~/Library/pnpm/store`<br>`~/Library/Caches/pnpm` | Rebuilds | **Yes, by pruning it.** |
| [Poetry’s cache and virtualenvs](https://siftmac.com/safe-to-delete/poetry-cache) | `~/Library/Caches/pypoetry`<br>`~/Library/Caches/pypoetry/virtualenvs` | Rebuilds | **Yes**, but know that it is two things. |
| [Swift Package Manager caches](https://siftmac.com/safe-to-delete/swift-package-manager-cache) | `~/Library/Caches/org.swift.swiftpm`<br>`<package>/.build` | Rebuilds | **Yes.** The shared cache in `~/Library/Caches/org.swift.swiftpm` and each package’s `.build` folder are fetched or built again. |
| [uv’s cache (~/.cache/uv)](https://siftmac.com/safe-to-delete/uv-cache) | `~/.cache/uv` | Rebuilds | **Yes, with uv’s commands.** |
| [Yarn’s cache](https://siftmac.com/safe-to-delete/yarn-cache) | `~/Library/Caches/Yarn`<br>`~/.yarn/berry`<br>`<project>/.yarn/cache` | Rebuilds | **Yes**, with one exception. |

## AI tools

| Folder | Where | Verdict | Short answer |
|---|---|---|---|
| [ChatGPT app data](https://siftmac.com/safe-to-delete/chatgpt-app-data) | `~/Library/Application Support/Codex`<br>`~/Library/Application Support/com.openai.codex`<br>`~/Library/Caches/com.openai.codex` | You decide | **Yes, for the caches.** |
| [Claude Code’s ~/.claude folder](https://siftmac.com/safe-to-delete/claude-code-folder) | `~/.claude`<br>`~/.claude/projects`<br>`~/.claude.json` | You decide | **No, not all of it.** |
| [Claude desktop app data](https://siftmac.com/safe-to-delete/claude-desktop-data) | `~/Library/Application Support/Claude`<br>`~/Library/Application Support/Claude/claude_desktop_config.json`<br>`~/Library/Logs/Claude` | You decide | **Partly.** The cache folders inside it are safe to clear with Claude quit, and they are usually the bulk of it. |
| [Codex’s ~/.codex folder](https://siftmac.com/safe-to-delete/codex-folder) | `~/.codex`<br>`~/.codex/sessions`<br>`~/.codex/archived_sessions` | You decide | **Partly.** `~/.codex` is the Codex CLI’s home: your `config.toml`, possibly your login, and every session it has saved. |
| [ComfyUI models](https://siftmac.com/safe-to-delete/comfyui-models) | `ComfyUI/models/checkpoints`<br>`ComfyUI/models/loras`<br>`ComfyUI/models/vae`<br>`~/ComfyUI-Shared` | You decide | **Yes, one by one.** |
| [DiffusionBee’s data folder](https://siftmac.com/safe-to-delete/diffusionbee-models) | `~/.diffusionbee`<br>`~/.diffusionbee/downloads`<br>`~/.diffusionbee/images` | You decide | **Yes, if you save your pictures first.** |
| [Gemini CLI’s ~/.gemini folder](https://siftmac.com/safe-to-delete/gemini-cli-folder) | `~/.gemini`<br>`~/.gemini/tmp`<br>`~/.gemini/history`<br>`~/.gemini/settings.json` | You decide | **No, not the whole folder.** |
| [Jan and GPT4All models](https://siftmac.com/safe-to-delete/jan-and-gpt4all-models) | `~/Library/Application Support/Jan/data`<br>`~/Library/Application Support/Jan/data/models`<br>`~/Library/Application Support/nomic.ai/GPT4All`<br>`~/.config/gpt4all.io` | You decide | **The models, yes. The folders, not blindly.** |
| [LM Studio models](https://siftmac.com/safe-to-delete/lm-studio-models) | `~/.lmstudio/models`<br>`~/.cache/lm-studio/models` | You decide | **Yes, model by model.** |
| [MLX models (mlx-lm)](https://siftmac.com/safe-to-delete/mlx-models) | `~/.cache/huggingface/hub/models--mlx-community--*`<br>`<project>/mlx_model` | You decide | **Yes, the downloaded ones.** |
| [NLTK and Keras data](https://siftmac.com/safe-to-delete/nltk-and-keras-data) | `~/nltk_data`<br>`~/.keras/datasets`<br>`~/.keras/models`<br>`~/.keras/keras.json` | Rebuilds | **Yes.** Both folders hold public files that a Python library downloaded: corpora and tokenizers for NLTK, datasets and pretrained weights for Keras. |
| [Ollama models](https://siftmac.com/safe-to-delete/ollama-models) | `~/.ollama/models` | You decide | **Yes, with `ollama rm`.** |
| [PyTorch Hub cache](https://siftmac.com/safe-to-delete/torch-hub-cache) | `~/.cache/torch/hub`<br>`~/.cache/torch/hub/checkpoints` | Rebuilds | **Yes.** Everything in `~/.cache/torch` was downloaded by PyTorch Hub or by a library such as torchvision. |
| [The Hugging Face cache](https://siftmac.com/safe-to-delete/hugging-face-cache) | `~/.cache/huggingface/hub`<br>`~/.cache/huggingface/datasets`<br>`~/.cache/huggingface/xet` | You decide | **Yes, but pick what goes.** |
| [Whisper speech models](https://siftmac.com/safe-to-delete/whisper-models) | `~/.cache/whisper`<br>`whisper.cpp/models/ggml-*.bin`<br>`whisper.cpp/models/*-encoder.mlmodelc` | Rebuilds | **Yes.** `~/.cache/whisper` only holds model weights that OpenAI’s Whisper package downloaded. |

## Virtual machines

| Folder | Where | Verdict | Short answer |
|---|---|---|---|
| [Parallels virtual machines (.pvm)](https://siftmac.com/safe-to-delete/parallels-virtual-machines) | `~/Parallels`<br>`~/Documents/Parallels`<br>`/Users/Shared/Parallels` | You decide | **Yes, if** you’re done with everything inside it. |
| [UTM virtual machines (.utm)](https://siftmac.com/safe-to-delete/utm-virtual-machines) | `~/Library/Containers/com.utmapp.UTM/Data/Documents` | You decide | **Yes, when you no longer need the guest.** |
| [VirtualBox virtual machines](https://siftmac.com/safe-to-delete/virtualbox-virtual-machines) | `~/VirtualBox VMs`<br>`~/Library/VirtualBox` | You decide | **Yes, VM by VM, from VirtualBox.** |

Data: [CC BY 4.0](LICENSE-DATA). Credit “Mac Folder Atlas (siftmac.com)” and link the entry’s page.
