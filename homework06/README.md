# Into the Kuberverse

In this project, we are building upon our previous project, which involves loading and retrieving meteorite landing site data from a Redis database server with a Flask application, by deploying the Flask app and Redis server in Kubernetes environment within TACC.

Downloading the Dataset

We need to first make sure to download the meteorite landing site data that was provided for the previous project to use and store in our Redis database server deployment. In order to do that, simply run the following command in your command line terminal:

wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json

## Description of Data

The data that we will be working with again is the Meteorite Landing Site Data. Here is a snippet of what it looks like:

```
  {
  "name": "Jennifer",
  "id": "10299",
  "recclass": "L5",
  "mass (g)": "539",
  "reclat": "-84.0579",
  "reclong": "69.9994",
  "GeoLocation": "(-84.0579, 69.9994)"
},
```

## Deploying in Kubernetes

To start our deployment in Kubernetes, log in to a Kubernetes cluster running on TACC through ISP02. Ssh into ISP02 and then ssh into coe332-k8s.tacc.cloud as shown:

`ssh <tacc_username>@isp02.tacc.utexas.edu`
`ssh <tacc_username>@coe332-k8s.tacc.cloud`

Next, clone this repository and cd into this folder using the following commands:

`git clone <the cloning url for this repository>`
`cd COE332_homework/homework06/`

With the files now in the Kubernetes cluster, we can start to deploy all of the yaml files. To do so simply run the following command on all 6 YAML files:

`kubectl apply -f <yaml-file>`

With all of our yaml files deployed, we can check if everything is up and running by using these commands:

```
kubectl get pods
kubectl get deployments
kubectl get services
```

If the STATUS is shown as Running and there are IP addresses under CLUSTER-IP, we are good to go!

## Using POST and GET methods in Kubernetes

In order to use the routes in our Flask app, we first need to enter the debug deployment using the following command:

`kubectl exec -it deployment-python-debug.yml -- /bin/bash`

Once in the debugger, we can now curl and use our Flask app.

## POST

The POST method of this route serves to load and store the data into the Redis database server. As such, it should be the first request made, which we can do by executing the command:

`curl <flask-service-IP>:5000/data -X POST`

Once requested, the data from ML_Data_Sample.json should be stored in the Redis database and a string should output confirming the successful completion of the process.

## GET

The GET method of this route serves to retrieve the data from the Redis database and output it. The command to execute this is shown below:

`curl <flask-service-IP>:5000/data`

`curl <flask-service-IP>:5000/data?start=<start-parameter>`

Be sure to replace <start-parameter> with the value of your choice.

The expected output format for the GET method for running the command are as follows:

`curl <flask-service-IP>:5000/data?start=10300`
  
```
  {
    "name": "Christina",
    "id": "10300",
    "recclass": "H5",
    "mass (g)": "4291",
    "reclat": "-38.1533",
    "reclong": "-46.7127",
    "GeoLocation": "(-38.1533, -46.7127)"
  }
```
Only numbers between 10001 and 10300 are accepted.
