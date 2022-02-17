# HYDRO-ANALYTICS

## Overview:
The goal of this project is to analyze the quality of the water and assess whether it is safe to analyze the samples or if the Mars lab should go on a boil water notice. This project is important in developing core skills including reading JSON data files into Python, performing calculations, interpreting data, and conducting unit tests. These are just a few of the many skills that this project encompasses and is vital for software engineers in their day-to-day job.

## Directions to Download Water Quality Data Set:
1) Click the link: https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
2) Log into TACC Computer
3) Move to the COE 332 Directory
4) Create a homework03 folder by using the mkdir command.
5) Use this command: `wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json` in order to download the file into the homework directory.

## Python Script Descriptions:
This project contains three files: `analyze_water.py` , `test_analyze_water.py` , `turbidity_data.json`.
- analyze_water.py contains three functions. The first function calculates the turbidity. The second function calculates the minimum decay time and determines whether the turbidity is below the threshold for safe use or not. Lastly, the main function provides structure and the ability to pull contents and dictionaries directly from the JSON file.
- test_analyze_water.py contains unit tests which ensure that the code and functions are working as expected. If minor changes are made to the code, these tests can be ran from this file in order to make sure that nothing is broken. Lastly, these unit tests test for edge cases.
- turbidity_data.json contains the water quality data that will be used for analysis and Python operations in this project.

## Instructions to Run Code:
1. Run analyze_water.py in the command line. You can do this by typing `python3 analyze_water.py` 
2. Run test_analyze_water.py in the command line. You can do this by typing `python3 analyze_water.py`

## Results:
The code outputs three key pieces of information:
- Average Turbidity
- Whether the Turbidity is above or below the safety threshold
- Minimum Decay Time required to return below safety threshold
