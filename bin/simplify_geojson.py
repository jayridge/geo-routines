#!/usr/bin/python
# -*- coding: utf8 -*-

#
# cmd line alternative w/o err checking
# egrep '^{ "type":' dork.json
#

import sys
import simplejson as json
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create an rtree from geojson.')
    parser.add_argument('-i', '--input', dest='input', help='geojson file, leave empty for stdin')
    args = parser.parse_args()

    if args.input:
        f = open(args.input, 'r')
    else:
        f = sys.stdin

    o = json.loads(f.read())
    for feature in o.get('features'):
         print json.dumps(feature)

    if args.input:
        f.close()
