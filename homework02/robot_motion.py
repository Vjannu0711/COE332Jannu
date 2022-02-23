import json
import math

with open('generate_random_sites.json', 'r') as f:
    ml_data = json.load(f)

mars_radius = 3389.5

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def compute_distance(ml_data, latitude, longitude, composition):
    lat_start = 16
    lon_start = 82
    legs = 0
    travel_time = 0
    for i in range(len(ml_data)):
        next_point_latitude = float(ml_data[i]['latitude'])
        next_point_longitude = float(ml_data[i]['longitude'])
        next_point_composition = str(ml_data[i]['composition'])
        distance_traveled = calc_gcd(next_point_longitude, next_point_latitude, lon_start, lat_start)
        trip_time = distance_traveled/10
        lon_start = next_point_longitude
        lat_start = next_point_latitude
        legs = legs + 1
        if(str(ml_data[i][composition]) == "stony"):
            sample_time = 1
        elif(str(ml_data[i][composition]) == "iron"):
            sample_time = 2
        else:
            sample_time = 3
        travel_time = travel_time + trip_time + sample_time
        print("leg =", i+1, ", time to travel = ", trip_time, " hr, time to sample = ", sample_time, " hr")
    print("number of legs =", legs, " total time elapsed =", travel_time, " hr")
    return(0)

print(compute_distance(ml_data['sites'], 'latitude', 'longitude', 'composition'))
