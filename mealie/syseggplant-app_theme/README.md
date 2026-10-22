# Mealie: SysEggplant theme variables

SysEggplant colours for [Mealie](https://mealie.io/) through its own theme environment variables. Each comment in the
file says what that colour paints.

Mealie's variables cover only these seven colour roles per mode. The page, cards, top bar, sidebar and type come from
the [Stylus theme](../syseggplant-stylus/), which shares these values.

## Install

Give the Mealie container these variables: as an `env_file` in Docker Compose, `--env-file` with `docker run`, or
`env` entries on a Kubernetes Deployment. Restart Mealie to apply them.

## Licence

AGPL-3.0-only.
