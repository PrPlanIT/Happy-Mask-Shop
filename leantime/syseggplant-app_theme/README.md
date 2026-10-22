# Leantime: SysEggplant server theme

A theme Leantime loads itself, selectable per user beside its built-in "More" and "Less" themes. Dark mode is an
eggplant ground with mint type; light mode is a green ground with plum type.

## Install

Leantime reads themes from `public/theme/<name>/`. Mount or copy this folder's contents so that the server has:

```
public/theme/syseggplant/theme.ini
public/theme/syseggplant/css/light.css
public/theme/syseggplant/css/dark.css
public/theme/syseggplant/css/custom.css
public/dist/images/background-syseggplant.png
```

The PNG is the card the theme picker shows; Leantime looks for it at that path by theme name.

Then pick **SysEggplant** under your profile's Theme tab, or set `LEAN_DEFAULT_THEME=syseggplant` to make it the
default (including the sign-in page). Clicking the card doesn't preview it live the way the built-in themes do;
it applies when you save.

The light and dark stylesheets build on Leantime's default theme with `@import`, so the default theme must stay in
place.

## Licence

AGPL-3.0-only.
