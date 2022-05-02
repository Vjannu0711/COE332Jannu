# Revitalization of Flask

## Description

In this project, we are given a large meteorite landing site dataset to work with. 
Our goal is to containerize and launch a Redis database server that we can both load data to and retrieve data from using a Flask application that we will containerize using a Dockerfile. 
With the emergence and widespread theme of big data and increasing prevalence of large datasets in today's world, having a reliable method and the skills necessary to store all of that data is important. 
Equivallently, having a method that updates, loads, and retrieves that data when necessary is paramount. 
This project aims to solve these core issues using a Redis database and Flask application to facilitate the storage and retrieval of data from large data sets like these.

## Downloading the Data Set

To get started, simply run the following command within your directory in the terminal: `wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json`


## Launch Redis Database

We first need to make sure we have redis installed. To do so, execute the command shown below:
```
pip3 install --user redis
```
Execute the following command to pull the redis:6 image:
```
docker pull redis:6
```
Launch the containerized Redis database server. 
We want to connect our assigned Redis port to the default Redis port and have it save 1 backup file every second to a /data folder. 
All of that can be done by running this command:
```
docker run -d -p <redis-port#>:6379 -v $(pwd)/data:/data:rw --name=<your-name>-redis redis:6 --save 1 1
```
NOTE: Be sure to replace `<redis-port#>` with your own/assigned redis port and `<your-name>` with your name.

You can check if it is up and running with `docker ps -a`, which should output a table of the format displayed below.
```
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS             PORTS                                                         NAMES
(Container ID) redis:6    "docker-entrypoint.s…"   (time created)  Up (time created)  0.0.0.0:<redis-port#>->6379/tcp, :::<redis-port#>->6379/tcp   "container-name"
```

Run the command below if any of the above is not found:
```
docker logs "container-name"
```

If you decide to use your own redis port, be sure to follow these instructions below to connect your Redis database server to your Flask application:
1) Run `docker inspect <container ID> | grep IPAddress` to find the IP (e.g. 172.xx.x.x)
2) Replace the redis client in the Flask app as: `redis.Redis(host='172.xx.x.x', port=6379)` and replace `172.xx.x.x` with the actual IP you find in the first part

## Pull/Build/Launch Flask Application

1. First start off by pulling the Flask app from Dockerhub using the following command: `docker pull <username>/<code>:<version>`

2. Before we can build or launch the Flask application, we need to add 2 new files to our directory:

	### Dockerfile:
	- Touch a file named "Dockerfile" into your directory by executing `touch Dockerfile` (file is already in repository)
	- Edit the newly created file: `emacs Dockerfile`
	- Enter the following lines of code and then save and exit:
	```
	FROM python:3.9
	RUN mkdir /app
	WORKDIR /app
	COPY requirements.txt /app/requirements.txt
	RUN pip install -r /app/requirements.txt
	COPY . /app
	ENTRYPOINT ["python"]
	CMD ["app.py"]
	```

	### requirements.txt:
	- Touch a file named "requirements.txt" into your directory by inputting `touch requirements.txt`
	- Open the newly created file `emacs requirements.txt`
	- Add these two lines of code and exit out of the file:
    ```
    Flask==2.0.3
    redis==4.2.1
    ```
  
3. Once those files have been added to your directory, you can build the container by running the following command: `docker build -t <username>/<code>:<version> .`

4. Once built, you can then run and launch the docker container by executing the command: `docker run --name "container-name" -d -p <port#>:5000 <username>/<code>:<version>`

Check if it is up and running with `docker ps -a`, which should output a table of the format displayed below:
```
CONTAINER ID   IMAGE                         COMMAND           CREATED         STATUS             PORTS                                             NAMES
(Container ID) <username>/<code>:<version>   "python app.py"   (time created)  Up (time created)  0.0.0.0:<port#>->5000/tcp, :::<port#>->5000/tcp   "container-name"
```

## Using POST and GET methods in the Flask Application

This Flask application only contains one route, `/data`, with two methods, `POST` and `GET`.

### POST
The `POST` method of this route serves to load and store the data into the Redis database server. Execute this command: `curl localhost:<port#>/data -X POST`

Once requested, the data from ML_Data_Sample.json should be stored in the Redis database and it will confirm that the data has been loaded to Redis.

### GET
The `GET` method of this route retrieves data from Redis and outputs it. Execute this command: `curl localhost:<post#>/data`

If the user wants to set a start query parameter for the data that outputs all the data starting at the parameter until the end, the following command should be run instead:
```
curl localhost:<post#>/data?start=<start-parameter>
```

Only numbers between 10001 and 10300 are accepted.

## Description of Data

The data that we have been working with all this time is meteorite landing site data. The following is an entry contained within the sample data:
  ```
  ...
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
  
As shown here, each entry in the dataset contains the name of the person that discovered and analyzed the meteorite, the ID number of the meteorite site, the classification of the meteorite, the mass of the meteorite, the latitudinal and longitudinal location of the meteorite, and the geolocation of the meteorite. All of this data is contained in one dictionary. The dataset we're working with includes 300 of these entries all within a list. 
That list is a value in the singular key:value pair in the dictionary that is this data set.
