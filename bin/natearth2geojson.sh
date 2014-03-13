#!/bin/bash

#
# natural earth attributes are in latin-1
#

if [ $# -ne 2 ]; then
    echo "usage: $0 input output"
    exit 1
fi

mkdir -p `dirname $2`
TMP=$2.tmp
./togeojson.sh $1 $TMP
iconv -f ISO_8859-1 -t UTF-8 $TMP > $2
rm $TMP
