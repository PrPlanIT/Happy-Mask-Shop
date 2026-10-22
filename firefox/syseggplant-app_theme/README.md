# Firefox: SysEggplant

A Firefox browser theme: eggplant toolbar, green frame, mint tab text.

## Install

`manifest.json` is the whole theme. Firefox installs themes packaged as an `.xpi`, which is a zip of this file:

```sh
zip SysEggplant.xpi manifest.json
```

- **Try it:** `about:debugging` → This Firefox → Load Temporary Add-on → pick `manifest.json`. It lasts until
  Firefox restarts.
- **Keep it:** Firefox only installs signed add-ons permanently; sign the `.xpi` through
  [addons.mozilla.org](https://addons.mozilla.org/developers/) (self-distribution), or use Firefox Developer Edition
  or Nightly with `xpinstall.signatures.required` set to `false`.

## Licence

AGPL-3.0-only.
