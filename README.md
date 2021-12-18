
# GKE interview docker and chart .
## Prerequisites :
* docker
* helm
* kubectl

### to build new docker image 
```bash
docker build --pull --rm -f "Dockerfile" -t amitzbb111/timezone:1.0.0 "."
```

### to install the chart run the following command:

```bash
helm upgrade --install  timezone -f ./timezone/values.yaml ./timezone
```

### to delete the chart run the following command 

```bash
helm delete timezone
```

