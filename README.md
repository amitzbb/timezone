
# GKE interview docker and chart .
## Prerequisites :
* docker
* helm
* kubectl

### to install the chart run the following command:

```bash
helm upgrade --install  timezone -f ./timezone/values.yaml ./timezone
```

### to delete the chart run the following command 

```bash
helm delete timezone
```

