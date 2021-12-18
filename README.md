
# Skybox terrafrom exercise .
## Prerequisites :
* docker
* helm

### to install terraform on centos:

```bash

```

#### clone the repository to your linux vm and move to the relvant directory 
```bash

```
#### make sure it works as expected
make sure your haproxy is up running using docker ps, open your chrome browser and enter the vm ip.
you will get hello world with the hostname of one of the 2 webservers refresh the page to see that roundrobin
engine is working.

##### haproxy dashboard http://hostip:/haproxy?stats admin:admin

###### you can also copy deployment.sh run chmod +x deployment.sh and excute the script ./deployment.sh this will clone the repo and run terraform
