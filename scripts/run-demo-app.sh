#!/usr/bin/env bash

podman run --rm -d \
       --name demo-app \
       --pod cloud-native-demo \
       --stop-signal=SIGINT \
       demo-app:1.0.0
