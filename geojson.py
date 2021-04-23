#! usr/bin/env python

from sys import argv
from os.path import exists
import json

script, in_file, out_file = argv

data = json.load(open(in_file), encoding='unicode-escape')

geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [float(d["lng"]), float(d["lat"])],
            },
        "properties" : d,
     } for d in data]
}


output = open(out_file, 'w', encoding='unicode-escape')
json.dump(geojson, output, ensure_ascii=False)
print(geojson)

