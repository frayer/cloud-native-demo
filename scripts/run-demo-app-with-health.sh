#!/usr/bin/env bash

podman run --rm -d \
       --name demo-app \
       --pod cloud-native-demo \
       --stop-signal=SIGINT \
       --health-cmd "curl --fail http://localhost:5000/ready || exit 1" \
       --health-interval 3s \
       --health-retries 1 \
       --health-start-period 1s \
       --health-timeout 2s \
       demo-app:1.0.0
