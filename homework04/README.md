# Globalization Containerization

## Description

We are given a data set containing the properties of various meteorite landings and we analyze the average mass of the meteors, the hemisphere they were found in, and their class. Since we have already finished writing the code, organized the output for readability, and made a unit test to test all of the functions used in the project. From these pieces, we can analyze the types of meteors present.

## Run Instructions

First, download these files from a Docker image. To get a Docker image, you can pull my existing Docker image from Docker Hub by executing this command:

    docker pull vjannu0711/ml_data_analysis:hw04

 To build your own Docker image instead, you would execute this command:

    docker build -t <username>/ml_data_analysis:1.0 .

 Now that you have the Docker image, you can run the code by executing the command:

    docker run --rm -v $PWD:/data username/ml_data_analysis:1.0 ml_data_analysis.py /data/Meteorite_Landings.json

To run the code for any given data, you can first run this command:

    wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json

to download the data to the directory, replacing the link with a link to your sample data. 
Then, build your own Docker image following the instructions listed above so that the new data set is included. 
You can then run the code again, replacing the name of the data file as so:

    docker run --rm -v $PWD:/data username/ml_data_analysis:1.0 ml_data_analysis.py /data/ML_Data_Sample.json

To test everything with pytest, you can go inside the container by running the commands:

    docker run --rm -it -v $PWD:/data username/ml_data_analysis:1.0 /bin/bash
    cd /data
    pytest

The data inside should look something like:

    {
      "meteorite_landings": [
        {
          "name": "Gerald",
          "id": "10001",
          "recclass": "H4",
          "mass (g)": "5754",
          "reclat": "-75.6691",
          "reclong": "60.6936",
          "GeoLocation": "(-75.6691, 60.6936)"
        },
        ....

Additionally, more Meteorite Landing data can be found in this link https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json and can be downloaded following the instructions above.

## ml_data_analysis.py

This script analyzes the meteorite landing data (Meteorite_Landings.json). It takes the data contained within the list of dictionaries, specifically analyzing:
- mass 
- longitude
- latitude
- class keys
to output the: 
- average mass of all meteorites in the data
- the number of meteorites that landed in each hemisphere
- and the number of meteorites of each class. 

It does this using 3 functions:
- ``compute_average_mass()`` takes all the values under the "mass (g)" key of each dictionary in the list and computes the average of those values. 
- ``check_hemisphere()`` takes the longitude and latitude keys of each dictionary in the list and determines whether the meteorite landed in the Northern or Southern Hemisphere, and then whether it landed in the Eastern or Western Hemisphere, and outputs the result of both. 
- ``count_classes()`` function takes the "recclass" key of each dictionary in the list and counts how many of each class are present in it, outputing a dictionary containing the class as a key and the count as the value. 

The expected output should look something like:

    Summary data following meteorite analysis:
    
    Average mass of 30 meteors:
    83857.3 grams
    
    Hemisphere summary data:
    There were 21 meteors found in the Northern & Eastern quadrant
    There were 6 meteors found in the Northern & Western quadrant
    There were 0 meteors found in the Southern & Eastern quadrant
    There were 3 meteors found in the Southern & Western quadrant
    
    Class summary data:
    The L5 class was found 1 times
    The H6 class was found 1 times
    The EH4 class was found 2 times
    The Acapulcoite class was found 1 times
    The L6 class was found 6 times
    The LL3-6 class was found 1 times
    The H5 class was found 3 times
    The L class was found 2 times
    The Diogenite-pm class was found 1 times
    The Stone-uncl class was found 1 times
    The H4 class was found 2 times
    The H class was found 1 times
    The Iron-IVA class was found 1 times
    The CR2-an class was found 1 times
    The LL5 class was found 2 times
    The CI1 class was found 1 times
    The L/LL4 class was found 1 times
    The Eucrite-mmict class was found 1 times
    The CV3 class was found 1 times
    
## test_ml_data_analysis.py

This script contains the unit tests for the previous script, ``ml_data_analysis.py``, and is used to test the functions for it. It tests to make sure the functions ``compute_average_mass()``, ``check_hemisphere()``, and ``count_classes()`` are arithmetically correct and output the correct values and data types. It also checks that there is an error when there should be an error. When running this script with pytest, all tests should pass.
