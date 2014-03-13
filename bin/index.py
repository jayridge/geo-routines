import sys
import re
from rtree import index
import ujson as json
import geojson
import argparse
from shapely.geometry import Polygon, asShape
from shapely import speedups

if speedups.available:
    speedups.enable()

'''
properties examples

natural earth
-------------
country {'ISO_A3': 'AGO', 'ADM0_A3': 'AGO', 'ISO_A2': 'AO', 'FeatureCla': 'Adm-0 country', 'POSTAL': 'AO', 'GU_A3': 'AGO', 'SUBUNIT': 'Angola', 'GDP_MD_EST': 110300.0, 'GEOUNIT': 'Angola', 'ne_10m_adm': 'AGO', 'MAP_COLOR': 1.0, 'ADM0_DIF': 0.0, 'TERR_': '', 'ABBREV': 'Ang.', 'GEOU_DIF': 0.0, 'LabelRank': 2, 'ScaleRank': 1, 'SU_A3': 'AGO', 'LEVEL': 2.0, 'ADMIN': 'Angola', 'FIPS_10_': 0.0, 'SU_DIF': 0.0, 'POP_EST': 12799293.0, 'SOVEREIGNT': 'Angola', 'NAME_FORMA': 'Republic of Angola', 'OID_': 82, 'NAME': 'Angola', 'SOV_A3': 'AGO', 'ISO_N3': 24.0, 'NAME_SORT': 'Angola', 'TYPE': 'Sovereign country'}

states/provinces { "OBJECTID": 1, "VertexCou": 262.000000, "ISO": "SOM", "NAME_0": "Somalia", "NAME_1": "Bari", "VARNAME_1": "", "NL_NAME_1
": "", "HASC_1": "SO.BR", "TYPE_1": "Gobolka", "ENGTYPE_1": "Region", "VALIDFR_1": "Unknown", "VALIDTO_1": "Present", "REMARKS_1": "", "Region": "", "RegionV
ar": "", "ProvNumber": 2001, "NEV_Countr": "Somalia", "FIRST_FIPS": "", "FIRST_HASC": "", "FIPS_1": "SO03", "gadm_level": 1.000000, "CheckMe": 0, "Region_Cod
": "", "Region_C_1": "", "ScaleRank": 5, "Region_C_2": "", "Region_C_3": "", "Country_Pr": "", "DataRank": 8, "Abbrev": "", "Postal": "BR", "Area_sqkm": 7001
4.100000, "sameAsCity": -99, "ADM0_A3": "SOM", "MAP_COLOR": 7, "LabelRank": 5, "Shape_Leng": 11.775567, "Shape_Area": 5.777993 }

urban { "Name_conve": "Aalborg", "MAX_POP_al": 101616.000000, "MAX_POP_20": 101616.000000, "MAX_POP_50": 0.000000, "MAX_POP_30":
 0.000000, "MAX_POP_31": 0.000000, "MAX_NatSca": 20.000000, "MIN_AreaKM": 76.000000, "MAX_AreaKM": 76.000000, "MIN_AreaMI": 29.000000, "MAX_AreaMI": 29.00000
0, "MIN_PerKM": 84.000000, "MAX_PerKM": 84.000000, "MIN_PerMI": 52.000000, "MAX_PerMI": 52.000000, "MIN_bb_xmi": 9.850000, "MAX_bb_xmi": 9.850000, "MIN_bb_xm
a": 10.033333, "MAX_bb_xma": 10.033333, "MIN_bb_ymi": 56.983333, "MAX_bb_ymi": 56.983333, "MIN_bb_yma": 57.100000, "MAX_bb_yma": 57.100000, "MEAN_bb_xC": 9.9
33411, "MEAN_bb_yC": 57.036154 }

zilow
-----

{ "STATE": "AK", "COUNTY": "Anchorage", "CITY": "Anchorage", "NAME": "Old Seward-Oceanview", "REGIONID": 274891.000000 }
'''

pmap = {
    'name':'name',
    'NAME':'name',           # naturalearth, zillow
    'NAME_1':'name',         # naturalearth
    'Name_conve':'name',     # naturalearth, trailing digits
    'ISO_A2':'iso',          # naturalearth
    'HASC_1':'hasc',         # naturalearth
    'FIPS_1':'fips',         # naturalearth
    'STATE':'state',         # zillow
    'COUNTY':'county',       # zillow
    'CITY':'city',           # zillow
}
def property_map(prop):
    global pmap
    newprop = {}
    for key in pmap.keys():
        if key in prop:
            newprop[pmap[key]] = prop[key]
    return newprop
    
def generator_function(f, verbose):
    counter = 0
    for line in f:
        try:
            obj = geojson.loads(line)
        except:
            print "Unexpected error:", sys.exc_info()
            continue
        properties = property_map(obj.get('properties'))
        geometry = obj.get('geometry')
        geom_type = geometry.get('type')
        if geom_type == 'Polygon':
            poly = asShape(geometry)
            bounds = poly.bounds
            feature = geojson.Feature(id=counter, geometry=poly, properties=properties)

            print counter, bounds, properties.get('name')
            counter += 1
            yield (counter, bounds, json.loads(geojson.dumps(feature)))
        elif geom_type == 'MultiPolygon':
            mpoly = asShape(geometry)
            for poly in mpoly:
                bounds = poly.bounds
                feature = geojson.Feature(id=counter, geometry=poly, properties=properties)

                print counter, bounds, properties.get('name')
                counter += 1
                yield (counter, bounds, json.loads(geojson.dumps(feature)))
        else:
            print "unsupported type", geom_type
            continue


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create an rtree from geojson.')
    parser.add_argument('-i', '--input', dest='input', help='geojson file, leave empty for stdin')
    parser.add_argument('-o', '--output', dest='output', required=True, help='path to rtree')
    parser.add_argument('-xw', '--overwite',  dest='overwrite', action='store_true')
    parser.add_argument('-v', dest='verbose', action='store_false')
    args = parser.parse_args()
    if args.verbose:
        print args

    f = None
    if args.input:
        f = open(args.input, 'r')

    file_idx = index.Rtree(args.output,
        generator_function(f or sys.stdin, args.verbose),
        overwrite=args.overwrite, interleaved=True)

    if f:
        f.close()
 
