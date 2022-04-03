from flask import Flask, request
import json
import logging
import redis

app = Flask(__name__)
meteor_data = {}

@app.route('/data',methods=['POST'])
def read_data_from_file():
    """
    This route reads the meteorite landings data JSON file and returns a statement that confirms that the data from the files have been read.
    """
    rd = redis.Redis(host='172.17.0.12', port=6379)
    logging.info("Data is being read.")
    global meteor_data
    with open('ML_Data_Sample.json' , 'r') as f:
        meteor_data =  json.load(f)
    for d in meteor_data['meteorite_landings']:
        rd.set(d['id'],json.dumps(d))
    return f'Data has been read from file\n'

@app.route('/data', methods=['GET'])
def get_all_names():
    """
    Iterates through a list of meteorite landings
    Returns:
    List of Names
    """
    rd = redis.Redis(host='172.17.0.12', port=6379)
    logging.info("Querying route to obtain all names...")
    list_data = []
    for i in range(10001, 10301, 1):
        list_data.append(json.loads(rd.get(i)))
    #BONUS ATTEMPT
    #start = request.args.get('start',0)
    #if start:
    #    try:
    #        start = int(start)
    #    except (ValueError):
    #        return f'Invalid start value! Start must be numeric (between 10001 and 10300, inclusive).\n'
    #list_data = []
    #while start <= 10000 + len(rd.keys()):
    #    list_data.append(json.loads(rd.get(start)))
    #    start += 1
    return json.dumps(list_data, indent=2)+'\n'
