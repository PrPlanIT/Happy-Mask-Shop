# Mealie: SysEggplant server theme

SysEggplant served by Mealie itself, for every user and device with nothing to install in the browser: page, cards,
top bar, sidebar, search, login card, recipe cards and buttons, light and dark, with Monofur as the type. It is the
same theme as the [Stylus version](../syseggplant-stylus/), compiled with its default settings.

| File | What it is |
|---|---|
| `syseggplant.css` | the theme stylesheet, Monofur embedded |
| `mealie-syseggplant.app_theme.env` | Mealie's `THEME_*` colours, which the stylesheet builds on |
| `link-theme.py` | copies Mealie's frontend and links the stylesheet into every page |
| `monof_tt.txt` | Monofur's licence text, served beside the font |

## How it works

Mealie has no setting for a custom stylesheet, but it can serve its frontend from another folder (`STATIC_FILES`).
`link-theme.py` runs once before Mealie starts, with Mealie's own image so the copy always matches the running
version: it copies the frontend to a shared volume, adds `syseggplant.css` and links it into each page. Mealie then
serves that copy. Upgrading Mealie needs nothing extra; the next start relinks the new frontend.

## Install: Docker Compose

Put this folder's files in `./syseggplant/` next to your `docker-compose.yml`, then:

```yaml
services:
  mealie-theme:
    image: ghcr.io/mealie-recipes/mealie:v3.28.0   # the same image as mealie
    entrypoint: ["python3", "/theme-files/link-theme.py", "/theme-files", "/theme/frontend"]
    volumes:
      - ./syseggplant:/theme-files:ro
      - mealie-theme:/theme

  mealie:
    image: ghcr.io/mealie-recipes/mealie:v3.28.0
    env_file: ./syseggplant/mealie-syseggplant.app_theme.env
    environment:
      STATIC_FILES: /theme/frontend
    volumes:
      - mealie-theme:/theme:ro
    depends_on:
      mealie-theme:
        condition: service_completed_successfully

volumes:
  mealie-theme:
```

Keep your existing `mealie` settings and volumes; these are the additions.

## Install: Kubernetes

Make a ConfigMap of the files (`kubectl create configmap mealie-theme --from-file=.`), set the `THEME_*` variables
from the env file on the Mealie container, and add:

```yaml
spec:
  initContainers:
    - name: theme
      image: ghcr.io/mealie-recipes/mealie:v3.28.0   # the same image as mealie
      command: ["python3", "/theme-files/link-theme.py", "/theme-files", "/theme/frontend"]
      volumeMounts:
        - { name: theme, mountPath: /theme }
        - { name: theme-files, mountPath: /theme-files, readOnly: true }
  containers:
    - name: mealie
      env:
        - { name: STATIC_FILES, value: /theme/frontend }
      volumeMounts:
        - { name: theme, mountPath: /theme, readOnly: true }
  volumes:
    - { name: theme, emptyDir: { sizeLimit: 64Mi } }
    - { name: theme-files, configMap: { name: mealie-theme } }
```

## Colours only

The env file alone recolours Mealie's highlights, buttons and status colours, without the page, cards, bars or type.

## Credits

Embeds the [Monofur](https://www.dafont.com/monofur.font) typeface by tobias b koehler, freeware that may be
distributed with its text file: [`monof_tt.txt`](monof_tt.txt).

## Licence

AGPL-3.0-only for the theme; Monofur keeps its own terms.
