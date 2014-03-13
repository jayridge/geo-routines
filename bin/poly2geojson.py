import sys
import os
import ujson as json
import geojson
import argparse
from parse_poly import parse_poly
from shapely.geometry import Polygon, asShape
from shapely import speedups

if speedups.available:
    speedups.enable()

counter = 0
dir = '/geo/rawdata/poly/'
files = os.listdir(dir)
for file in files:
    if not os.path.isfile(dir+file): continue
    f = open(dir+file, 'r')
    try:
        name, poly = parse_poly(f.readlines())
        feature = geojson.Feature(id=counter, geometry=poly, properties=dict(name=name))
        print geojson.dumps(feature)
    except:
        pass
    f.close()
    counter += 1

