import pandas as pd
import numpy as np
import matplotlib
from datetime import datetime

#colecting data and saving to csv files

#parks
url_parks = 'https://data.cityofchicago.org/resource/2eaw-bdhe.json'
parks = pd.read_json(url_parks)
parks.to_csv("parks.csv", index = False)

#air quality
url_air_quality = 'https://data.cityofchicago.org/resource/i9rk-duva.json'
air_quality = pd.read_json(url_air_quality)
air_quality.to_csv("air_quality.csv", index = False)

#energy use
url_energy = "https://data.cityofchicago.org/resource/jn94-it7m.json"
energy_use = pd.read_json(url_energy)
energy_use.to_csv("energy.csv", index = False)

#traffic
url_traffic = "https://data.cityofchicago.org/resource/pf56-35rv.json"
traffic = pd.read_json(url_traffic)
traffic.to_csv("traffic.csv", index = False)

#crime
url_crime = "https://data.cityofchicago.org/resource/dfnk-7re6.json"
crime = pd.read_json(url_crime)
crime.to_csv("crime.csv", index = False)

#log
time = datetime.now()
log_file = open('data_log.txt', "w")
log_file.write("Sociome dataset\n")
update = "Last update: " + str(time)
log_file.write(update)