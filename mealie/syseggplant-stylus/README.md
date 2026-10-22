# Mealie: SysEggplant

SysEggplant for the [Mealie](https://mealie.io/) recipe manager, light and dark: page, cards, top bar, sidebar,
search, login card, recipe cards and buttons, with Monofur as the type.

**Needs:** [Stylus](https://github.com/openstyles/stylus).

## Install

Open the `.user.css` file's raw view and let Stylus install it. It matches Mealie on its default port, 9000; for any
other address, add it under the style's "Applies to" in Stylus.

## Settings

Every colour is a setting under the style's gear icon. Settings named `THEME_*` are Mealie's own environment
variables; the rest are "Stylus only": Mealie has no setting for them. "Monofur everywhere" switches the whole app
to Monofur.

To serve the whole theme from Mealie itself, for every user, use the
[server theme](../syseggplant-app_theme/) instead.

## Credits

Embeds the [Monofur](https://www.dafont.com/monofur.font) typeface by tobias b koehler, freeware that may be
distributed with its text file: [`monof_tt.txt`](monof_tt.txt).

## Licence

AGPL-3.0-only for the style; Monofur keeps its own terms.
