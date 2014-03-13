import sys
import os
import tornado.options
import tornado.web
from tornado.escape import utf8
import settings
import logging
import time
import simplejson as json
from rtree import index
import geojson
from shapely.geometry import Point, Polygon, asShape
from shapely import speedups
from lib.fips import fips_codes

if speedups.available:
    speedups.enable()

class BaseHandler(tornado.web.RequestHandler):
    def get_int_argument(self, name, default=None):
        value = self.get_argument(name, default=default)
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    def error(self, status_code=500, status_txt=None, data=None):
        """write an api error in the appropriate response format"""
        self.api_response(status_code=status_code, status_txt=status_txt, data=data)

    def api_response(self, data, status_code=200, status_txt="OK"):
        """write an api response in json"""
        self.set_header("Content-Type", "application/json; charset=utf-8")
        self.finish(json.dumps(dict(data=data, status_code=status_code, status_txt=status_txt)))

class GeoHandler(BaseHandler):
    def get(self):
        lat = float(self.get_argument("lat"))
        lng = float(self.get_argument("lng"))
        # left, bottom, right, top
        bbox = (lng, lat, lng, lat)
        point = Point(lng, lat)
        tmp = [(n.object, n.bbox) for n in _idx.intersection(bbox, objects=True)]
        results = []
        for x,b in tmp:
            print x.get('properties',{}).get('name'), b
            shp = asShape(x.get('geometry'))
            if point.within(shp):
                props = x.get('properties',{})
                fips = props.get('fips')
                if fips:
                    fips_data = fips_codes.get(fips)
                    fips_parent = fips_codes.get(fips[:2]+'00')
                    props['fips_data'] = fips_data
                    props['fips_parent'] = fips_parent
                    print "FIPS", fips_data, fips_parent
                results.append(dict(name=x.get('properties',{}).get('name'),
                    bbox=b,properties=props))
        self.api_response(results)

class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.tpl")

if __name__ == "__main__":
    tornado.options.define("port", default=8888, help="Listen on port", type=int)
    tornado.options.define("rtree", default=settings.get('rtree_file'), help="path to rtree", type=str)
    tornado.options.parse_command_line()
    logging.getLogger().setLevel(settings.get('logging_level'))

    logging.info("loading rtree index: %r" % tornado.options.options.rtree)
    _idx = index.Index(tornado.options.options.rtree)

    settings = {
        'static_path': os.path.join(os.path.dirname(__file__), "www"),
        'template_path': os.path.join(os.path.dirname(__file__), "www"),
        'debug': True,
    }
    application = tornado.web.Application([
        (r"/$", IndexHandler),
        (r"/geo$", GeoHandler),
    ], **settings)
    application.listen(tornado.options.options.port)
    logging.info("listening on %r" % tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()
