#!/usr/bin/env bash

podman run --rm -d \
       --name redis \
       --pod cloud-native-demo \
       redis
