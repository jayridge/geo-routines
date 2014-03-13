import sys
import re
import geojson
import shapely
from shapely.geometry import MultiPolygon
from shapely import speedups

if speedups.available:
    speedups.enable()


pattern = r""".*VALUES \('([^']+)', ([0-9]+),.*MULTIPOLYGON\(\(\(([^\)]+)"""
pattern = r""".*VALUES \('([^']+)', ([0-9]+),.*(MULTIPOLYGON[^']+)"""
sql_prog = re.compile(pattern)

def parse_sql(sql, id=None):
    global sql_prog
    match = sql_prog.match(sql)
    if match and len(match.groups()) == 3:
        name = match.group(1).strip()
        level = int(match.group(2))
        try:
            poly = shapely.wkt.loads((match.group(3)))
        except:
            print "could not load poly", name, level
            return None
        if not poly.is_valid:
            print "poly not valid", name, level
            return None
        bounds = poly.bounds
        print "OK", name, level
        return geojson.Feature(id=id, geometry=poly,
            properties=dict(name=name, admin_level=level))
    return None


i = 1 # line_no
for sql in sys.stdin:
    feature = parse_sql(sql, id=i)
    i += 1
    if feature:
        pass
        #print geojson.dumps(feature)
 
