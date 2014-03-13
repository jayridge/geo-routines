#!/bin/bash

apt-get update
apt-get upgrade
apt-get install -y xfsprogs
apt-get install -y openjdk-6-jdk
apt-get install -y build-essential
apt-get install -y g++
apt-get install -y python-dev
apt-get install -y python-pip
apt-get install -y libpq-dev
apt-get install -y libprotobuf-dev
apt-get install -y protobuf-compiler
apt-get install -y libtokyocabinet-dev
apt-get install -y libgeos-dev
apt-get install -y gdal-bin
pip install tornado
pip install protobuf
pip install imposm
pip install shapely
pip install geojson
pip install Rtree
pip install ujson

