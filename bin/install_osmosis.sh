#!/bin/bash

wget http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.tgz
tar xvfz osmosis-latest.tgz
rm osmosis-latest.tgz
cd osmosis-*
chmod a+x bin/osmosis

wget -O lib/default/borderextract-1.2.jar http://www.general-bytes.com/be/borderextract-1.2.jar
wget -O lib/default/guava-10.0.1.jar http://search.maven.org/remotecontent?filepath=com/google/guava/guava/10.0.1/guava-10.0.1.jar

