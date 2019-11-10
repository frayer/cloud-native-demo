# cloud-native-demo

* Deploy with `kubectl run`
* port-forward to consume
* Note how that if you delete the Pod it comes right back
* Scale the deployment from the command line
* Capture the resulting deployment with `kubectl get` and store to file
* Delete existing deployment and modify the declarative Deployment to have an initial replica count of 3
* Modify deployment to set environment variables
* Define a Service and Ingress
* Try to hit an endpoint which interacts with Redis (should error since redis isn't running)
* Deploy a single node Redis and expose it at a service with `kubectl`
* Configure liveness and readiness probes
