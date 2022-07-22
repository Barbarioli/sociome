import pandas as pd
import numpy as np

def extract_location(data):
  n_entities = data.shape[0]
  lat_col = []
  lon_col = []
  for i in range(n_entities):
    location = data.location[i]
    try:
      #print(location['latitude'])
      lat_col.append(location['latitude'])
      lon_col.append(location['longitude'])
    except:
      lat_col.append(np.nan)
      lon_col.append(np.nan)
  data['latitude'] = lat_col
  data['longitude'] = lon_col
  return data