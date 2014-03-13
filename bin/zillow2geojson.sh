#!/bin/bash

find /geo/rawdata/zillow.com/ -name '*.shp'| xargs -n1 -I {} sh -c 'FILE=`basename {}`; /geo/bin/togeojson.sh {} /geo/geojson/zillow.com/${FILE%%.*}.json'
