# 
# Download and extract raw data
#

naturalearth:
	@mkdir -p naturalearthdata.com
	@wget http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/10m-cultural.zip
	@unzip 10m-cultural.zip -d naturalearthdata.com
	@rm 10m-cultural.zip

simplegeo:
	@mkdir -p simplegeo.com
	@wget http://s3.amazonaws.com/simplegeo-public/SimpleGeo_Neighborhoods_20110817.zip
	@unzip SimpleGeo_Neighborhoods_20110817.zip -d simplegeo.com
	@rm SimpleGeo_Neighborhoods_20110817.zip

tiger:
	@wget -r ftp://ftp2.census.gov/geo/tiger/TIGER2011/STATE/
	@wget -r ftp://ftp2.census.gov/geo/tiger/TIGER2011/COUNTY/
	@wget -r ftp://ftp2.census.gov/geo/tiger/TIGER2011/COUSUB/
	@wget -r ftp://ftp2.census.gov/geo/tiger/TIGER2011/PLACE/
	@find ftp2.census.gov/ -name '*.zip'|xargs -n1 -I {} sh -c "unzip -o {} -d \`dirname {}\`"

openstreetmap:
	@mkdir -p openstreetmap.org
	@wget -O openstreetmap.org/planet-latest.osm.pbf http://planet.openstreetmap.org/pbf/planet-latest.osm.pbf

geofabrik:
	@mkdir -p geofabrik.de
	@wget -O geofabrik.de/europe.osm.pbf http://download.geofabrik.de/osm/europe.osm.pbf
	@wget -O geofabrik.de/africa.osm.pbf http://download.geofabrik.de/osm/africa.osm.pbf
	@wget -O geofabrik.de/asia.osm.pbf http://download.geofabrik.de/osm/asia.osm.pbf
	@wget -O geofabrik.de/australia-oceania.osm.pbf http://download.geofabrik.de/osm/australia-oceania.osm.pbf
	@wget -O geofabrik.de/central-america.osm.pbf http://download.geofabrik.de/osm/central-america.osm.pbf
	@wget -O geofabrik.de/south-america.osm.pbf http://download.geofabrik.de/osm/south-america.osm.pbf
	@wget -O geofabrik.de/canada.osm.pbf http://download.geofabrik.de/osm/north-america/canada.osm.pbf
	@wget -O geofabrik.de/us-midwest.osm.pbf http://download.geofabrik.de/osm/north-america/us-midwest.osm.pbf
	@wget -O geofabrik.de/us-northeast.osm.pbf http://download.geofabrik.de/osm/north-america/us-northeast.osm.pbf
	@wget -O geofabrik.de/us-pacific.osm.pbf http://download.geofabrik.de/osm/north-america/us-pacific.osm.pbf
	@wget -O geofabrik.de/us-south.osm.pbf http://download.geofabrik.de/osm/north-america/us-south.osm.pbf
	@wget -O geofabrik.de/us-west.osm.pbf http://download.geofabrik.de/osm/north-america/us-west.osm.pbf

zillow:
	@mkdir -p zillow.com
	@python scripts/zillow_urls.py | xargs -n1 wget --directory-prefix=zillow.com 
	@find zillow.com/ -name '*.zip'|xargs -n1 -I {} sh -c "unzip -o {} -d \`dirname {}\`"

fips:
	@mkdir -p fips
	@wget -O fips/fips-all.txt http://efele.net/maps/fips-10/data/fips-all.txt
	@cd fips; cat fips-all.txt | awk -F _ 'BEGIN {OFS = "\t"} {print $$1, $$4, $$5, $$8}' > fips.tab
