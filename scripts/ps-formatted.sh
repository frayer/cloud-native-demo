#!/usr/bin/env bash

# An abbreviated version of `podman ps` that scales up in font size nicely for
# demos.
podman ps --watch 1 --format "table {{.ID}}  {{.Names}}  {{.Status}}"