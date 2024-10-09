#!/usr/bin/env bash

podman pod create \
    --name cloud-native-demo \
    --publish 8080:5000
