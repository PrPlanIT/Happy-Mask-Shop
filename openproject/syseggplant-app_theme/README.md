# OpenProject: SysEggplant

Adds SysEggplant to OpenProject's colour presets (Administration → Design), beside "OpenProject", "OpenProject Gray"
and "OpenProject Navy Blue". In dark mode, where OpenProject normally swaps the header and sidebar to greys, it
keeps the eggplant and switches the accent to mint.

## Install

Mount the file into OpenProject's initializers, named so it loads after OpenProject's own:

```
/app/config/initializers/zz_color_themes.rb
```

Restart OpenProject, then pick **SysEggplant** in Administration → Design and save. Selecting it again after an
update re-applies its colours.

## Licence

AGPL-3.0-only.
