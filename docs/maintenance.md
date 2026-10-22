# Maintenance

How this repository is laid out, named and versioned. Follow it when adding or updating a theme.

## Layout

1. **The top level holds no theme files.** Only `README.md`, `LICENSE`, `docs/` and one folder per application.
2. **One folder per installable mod:** `<application>/<themename>-<context>/`. An application with more than one mod has one sibling folder per mod, each named for what it is.
3. **Each mod folder holds the standalone installable file and a `README.md` beside it.** The README says what the mod is, what it needs, how to install it, any settings to enter, and credits the original it is built on.

```
discord/syseggplant-quickcss/
├── README.md
└── discord-kaleidoscope-syseggplant.quickcss.css
```

4. **Screenshots go in the mod folder's `screenshots/`**, named `<application>-<themename>-<variant>.png` (`leantime-syseggplant-dark.png`). The mod's README shows them, and [`gallery.md`](gallery.md) lists every one.

## Naming

1. **Installable files are named `<application>-<mod>-<themename>.<context>.<ext>`**, so a file still makes sense once downloaded on its own. `<mod>` names the original the theme is built on and is left out when the theme is entirely ours.
2. **The context says how the theme gets in:**
   - `app_theme`: the application loads it itself (its theme, colour, settings or plugin mechanism).
   - `stylus`: a userstyle for the Stylus browser extension.
   - `quickcss`: CSS for a Discord client mod (Vencord, Vesktop, BetterDiscord).
3. **Hyphens separate parts; underscores join a descriptive phrase into one part.** `homeassistant-dark_mode-syseggplant.stylus.user.css`, `syseggplant-app_theme/`
4. **Product and project names are one word, as the product writes its own identifier:** `homeassistant`, `searxng`, `vscode`, `freecommander`, `pvediscorddark`. Underscores are for descriptions (`dark_mode`, `app_theme`), not names.
5. **Everything is lowercase.**
6. **Stylus files end in `.user.css`.** Stylus offers to install any link ending in `.user.css`, so clicking the raw file installs it.
7. **A host that dictates its own file names keeps them**, such as Firefox's `manifest.json` and Leantime's `theme.ini` and `css/`.

## Versions

1. **A theme's versions are its commit history, not extra files.** A newer palette replaces the file in a new commit; the old one stays readable in `git log`. SysEggplant's first palette (lime and purple, once called "OG") is the earliest version of each file it existed for, not a separate theme.
2. **A separate theme gets its own folder.** Only when it is a different theme, not a newer version of one.
3. **Author date is when that version was made; committer date is when it was committed here.** History imported from before this repository existed keeps that split, so the record is honest about both.
4. **Every backdated commit says where its date came from** in the commit body: an archive timestamp, a date or version in the file or its original name, an export record, or "approximate" with the reason.

## Publishing

1. **No addresses or internal hostnames.** Userstyles match by port or public domain (`regexp("https://.*:9443/.*")`), never by a private IP or LAN name, so anyone can install them unchanged. This applies to every version in the history, not only the latest.
2. **Settings exports carry only theme keys.** A VS Code or app settings file is reduced to its colour, token and font settings before it is committed.
3. **Credit the original.** A mod built on someone else's work names its author and links the original in its README, and keeps the original's licence notice where it has one.

## Self-contained

1. **Everything a theme loads lives in its installable file.** Remote `@import`s are replaced by the CSS they load, and remote images are embedded as data URIs, so the file works pasted on its own with no network and no third-party host.
2. **The README records each vendored asset**: its original URL, where the copy came from, and the date it was taken.
3. **Dead links are recovered, not dropped.** From the source repository's history, or from the Wayback Machine, and the README says which.

## Licensing

1. **The repository is AGPL-3.0-only**, like the rest of our projects.
2. **Permissive bases keep their notices.** A mod built on MIT or WTFPL work keeps the original copyright and licence notice in the file header and its README; our changes fall under the repository licence.
3. **Bases with no licence ship with attribution, outside the repository licence.** Their file header and README say they are the original author's work, shared with attribution, and not covered by AGPL-3.0-only.
