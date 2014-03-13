#!/bin/bash

#
# common geojson output format
#

if [ $# -ne 2 ]; then
    echo "usage: $0 input output"
    exit 1
fi

OUT=$2.tmp
echo ogr2ogr -wrapdateline -explodecollections -t_srs EPSG:4326 -f "GeoJSON" $2 $1
ogr2ogr -wrapdateline -t_srs EPSG:4326 -f "GeoJSON" $OUT $1
egrep '^{ "type":' $OUT > $2
rm $OUT
