# Discord: SysEggplant

SysEggplant for Discord, built on spinfish's Kaleidoscope theme.

**Needs:** [Vencord](https://vencord.dev/), [Vesktop](https://github.com/Vencord/Vesktop) (Vencord built in) or
[BetterDiscord](https://betterdiscord.app/).

## Install

The file is large (about 4 MB) because every image and stylesheet it uses is embedded in it, so it keeps working
even when the sites it came from go offline. Loading it as a file is smoother than pasting it.

- **Vencord / Vesktop:** Settings → Vencord → Themes → Open Themes Folder, drop the `.css` file in, then enable it.
  Or paste it into QuickCSS.
- **BetterDiscord:** paste it into Settings → Custom CSS.

## Credits

- [Kaleidoscope](https://github.com/spinfish/kaleidoscope), Copyright (c) 2021 spinfish, MIT License.
- [Discolored](https://github.com/nyri4/Discolored) by nyri4, WTFPL.
- [GT-RevertRebrand](https://github.com/Goose-Nest/GT-RevertRebrand), Copyright (c) 2021 GooseNest, MIT License.
- [css-snippets](https://github.com/spinfish/css-snippets), Copyright (c) 2021 spinfish, MIT License.
- Embedded Discord interface artwork belongs to Discord.

## Embedded assets

[`vendored_assets.json`](vendored_assets.json) lists every embedded file: its original URL, where the copy came
from and when it was taken.

- `lily.png` (a Discord attachment) is no longer online; it was recovered from the Wayback Machine.
- The theme also imported Better-Badges, whose stylesheet was deleted upstream in July 2021, before this theme was
  made. It never loaded, so it is noted in the file but not embedded.

## Licence

AGPL-3.0-only for the SysEggplant changes; the works above keep their own licences.
