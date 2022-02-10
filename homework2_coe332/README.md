# **MARS JOURNEY ROBOT MOTION AND TRACKING**

This repository contains three files: `random_sites.py`, `generate_random_sites.json`, `robot_motion.py`
This project is important in developing my skills of reading files and writing into JSON files using Python. In the real world, reading in large datasets, data manipulation, and generating structured data are very common tasks of countless IT professions including data scientists and software engineers.
This project gives me incredible exposure and practice to these fundamentals.

*random_sites.py* contains three functions total that randomly generate a latitude, longitude, and composition for meteorites 5 times. This information is then stored in a dictionary. This dictionary is stored in the JSON file called *generate_random_sites.json*.

*robot_motion.py* takes the information from the generate_random_sites.json file and reads it. It outputs the travel data and trip information of the robot that would travel to and sample each meteorite.

In order to properly execute the code as intended, run the random_sites.py script first in order to generate the generate_random_sites.json JSON file with the sites dictionary created from the python file. Then, run the robot_motion.py file in order to ouput and view the trip data and information of the robot.
