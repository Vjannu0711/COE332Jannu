import json
from random import seed
import random

def rand_composition(): # randomly selects a composition from the list of 3 compositions
    list = ["stony", "iron", "stony-iron"]
    val = random.choice(list)
    return val
def rand_latitude(): # randomly generates a latitude for the given site
    val = random.random() # generates a floating point number between 0 and 1
    val = 16 + (val*2)
    return val
def rand_longitude(): # randomly generates a longtiude for the given site
    val = random.random()
    val = 82 + (val*2)
    return val

meteorites_data = {}
meteorites_data['sites'] = []
# append and generate the sites and its respective values
for i in range(1,6):
    meteorites_data['sites'].append({'site_id': i, 'latitude': rand_latitude(), 'longitude' : rand_longitude(), 'composition': rand_composition()})

with open('generate_random_sites.json', 'w') as out:
    json.dump(meteorites_data,out,indent=2)
