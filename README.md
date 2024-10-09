# cloud-native-demo

A simple Flask application to demonstrate features of Container environments.
There are various HTTP endpoints to exercise features of the application however
they do not follow typical REST semantics. Intead, all are `HTTP GET` requests
to simplify demostrations when using `curl` CLI commands.

1. `/` - returns the application name, version, and a handful of environment variables
1. `/counter` - increments a counter
1. `/counter/clear` - resets the counter
1. `/live` - always returns a `200 OK` success code but with a delay determined by the `/live/<delay>` endpoint
1. `/live/{delay}` - sets the delay on the liveness probe to {delay} seconds
1. `/ready` - returns the readiness probe

# Demonstrations

- Pulling Container Images
  - https://hub.docker.com/
- Running a Container
  - Explain common arguments on `podman run` command
- Isolation of Container Environments (file system, process, user, network)
  - Assuming host machine is MacOS or Windows, show different between host, VM, and Container environments
  - Delete container file system to show immutability
  - Process visibility between host and container
  - User aliasing between host and container
  - Port mapping from container to host
- Building Container Images
  - Explain the background behind the file names of `Dockerfile` and `Containerfile`
  - Walk through statements in `Containerfile`
  - Explain common arguments on `podman build` command
  - Build different versions of a Container Image
- Container Image Layers
  - Explore the metadata of a Container Image
    - `podman image save -o demo-app.tar demo-app:1.0.0`
    - `tar -O -xf demo-app.tar manifest.json`
- Health Checks
