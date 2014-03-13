From: nate@path.com Nathan Folkman 
To: jayridge@gmail.com James Ridgeway 
Date: Wed, 22 Feb 2012 14:51:21 -0500 
Subject: Fwd: Context API 
 
i suck, forgot about this email. not sure if there's much in here that would help given the progress you've already made however.

Begin forwarded message:

> From: Ben Standefer <ben@urbanairship.com>
> Subject: Re: Context API
> Date: February 7, 2012 11:45:50 AM PST
> To: Nathan Folkman <nate@path.com>
> Cc: Sasha Mace <sasha@urbanairship.com>, Matt Van Horn <mvanhorn@path.com>, Dave Morin <dave@path.com>
> 
> Sure.  Some great open source datasets are listed below.  Also, along with the data, here are some examples of classes you could implement to make better sense of the data (identify the correct fields for name, abbreviation, etc.): https://gist.github.com/5112cdc36df164b49d27.  There is nothing proprietary in these classes, and all the data in them can be gleaned from reading the docs for each individual data source, but this should save you some time and grunt work.  Before doing anything with the data, we normally convert all the Shapefiles to GeoJSON (http://geojson.org/geojson-spec.html) to make it a little more easy for all the engineers to deal with the data down the road.
> 
> Feel free to ping me on XMPP (benstandefer@gmail.com) or AIM (aguynamedben) as you go if you have any questions about wrangling this open-source data.  We do use a premium provider of neighborhoods data (Factle), but it's kind of a one-man shop zany professor from Berkeley, with an ambiguous and vague license.  I could introduce you to him if you'd like.  Maponics (http://www.maponics.com/) seems like the most legit providers of premium polygon data, and they'll even go out and map things for you if you have a specific interest.
> 
> Hopefully this helps.
> 
> -Ben
> 
> 
> =====
> 
> WORLDWIDE efele.net Timezone Data
> Source: http://efele.net/maps/tz/world/
> 
> Timezone Data
>   Directory: /data/efele.net/
>   Files matching: tz_world_mp.shp
> 
> =====
> 
> WORLDWIDE Natural Earth
> Source: http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/10m-cultural.zip
> Docs: http://www.naturalearthdata.com/downloads/10m-cultural-vectors/
> 
> Natural Earth Admin 1 Data (worldwide states and provinces)
>   Directory: /data/naturalearthdata.com/20100430/10m_cultural/
>   Files matching: 10m_admin_1_states_provinces_shp.shp
> 
> Natural Earth Admin 0 Data (worldwide countries)
>   Directory: /data/naturalearthdata.com/20100430/10m_cultural/
>   Files matching: 10m_admin_0_countries.shp
> 
> Natural Earth Urban Area Data (worldwide metropolitan areas)
>   Directory: /data/naturalearthdata.com/20100430/10m_cultural/
>   Files matching: 10m_urban_areas_landscan.shp
> 
> =====
> 
> SimpleGeo Non-US Neighborhoods (open ODbL license)
> Source: http://s3.amazonaws.com/simplegeo-public/SimpleGeo_Neighborhoods_20110817.zip
> Docs: http://blog.simplegeo.com/2011/08/05/its-a-beautiful-day-in-the-neighborhood/ and http://blog.simplegeo.com/2011/08/18/more-neighborhoods/
> 
> Non-US neighborhoods
>   Directory: /data/simplegeo.com/neighborhoods/
>   Files matching: SG_.*.json (SG_LocalAdmin_Berlin.json, SG_Suburbs_Algiers.json, etc.)
> 
> =====
> 
> US-ONLY Tiger/LINE 2009 data (2010 is out now, some things might have changed since 2009, but it's generally similar)
> Source: http://www.census.gov/geo/www/tiger/shp.html
> Docs: http://www.census.gov/geo/www/tiger/tgrshp2009/TGRSHP09.pdf (they are a bit intense, I recommend searching for the filename you're dealing with)
> 
> Tiger/LINE State Data
>   Directory: /data/tigerline/2009/
>   Files matching: tl_.*_us_state.shp (tl_2009_us_state.shp)
> 
> Tiger/LINE County Data
>   Directory: /data/tigerline/2009/
>   Files matching: tl_.*_us_county.shp (tl_2009_us_county.shp)
> 
> Tiger/LINE Zip Data
>   Directory: /data/tigerline/2009/
>   Files matching: tl_.*_us_zcta5.shp (tl_2009_us_zcta5.shp)
> 
> Tiger/LINE Place Data (towns, etc., not places like "McDonald's")
>   Directory: /data/tigerline/2009/\d\d_.*
>   Files matching: tl_.*_\d\d_place.shp (tl_2009_01_place.shp, etc.)
>   Note: These are located in individual state dirs inside the 2009 dir.
> 
> Tiger/LINE Tract Data
>   Directory: /data/tigerline/2009/
>   Files matching: tl_\d\d\d\d_\d\d_tract.shp (tl_2009_01_cd111.shp)
>   Note: There are tract shape files located inside the individual state dirs as well, but the regex won't pick them up since they look like tl_2009_01001_tract00.shp.
> 
> Tiger/LINE Congressional District Data
>   Directory: /data/tigerline/2009/
>   Files matching: tl_\d\d\d\d_\d\d_cd111.shp (tl_2009_01_cd111.shp)
> 
> Tiger/LINE Upper Legislative District Data
>   Directory: /data/gov.census.tiger/2009/
>   Files matching: tl_\d\d\d\d_\d\d_sldu.shp (tl_2009_01_sldu.shp)
> 
> Tiger/LINE Lower Legislative District Data
>   Directory: /data/tigerline/2009/
>   Files matching: tl_\d\d\d\d_\d\d_sldl.shp (tl_2009_01_sldl.shp)
> 
> Tiger/LINE Unified School District Data
>   Directory: /data/tigerline/2009/
>   Files matching: tl_\d\d\d\d_\d\d_unsd.shp (tl_2009_01_unsd.shp)
>   Note: There's also tl_2009_01_unsd00.shp, but I have no idea what it's for.
> 
> Tiger/LINE Elementary School District Data
>   Directory: /data/tigerline/2009/
>   Files matching: tl_\d\d\d\d_\d\d_elsd.shp (none)
>   Note: It doesn't appear that we actually have any of this type of data for 2009.
> 
> Tiger/LINE Secondary School District Data
>   Directory: /data/tigerline/2009/
>   Files matching: tl_\d\d\d\d_\d\d_scsd.shp (none)
>   Note: It doesn't appear that we actually have any of this type of data for 2009.
> 
> Tiger/LINE Precinct Data
>   Directory: /data/tigerline/2009/\d\d_.*
>   Files matching: tl_\d\d\d\d_\d\d\d\d\d_vtd00.shp (tl_2009_01001_vtd00.shp)
>   Note: These are located in the individual state dirs in the 2009 dir.
> 
> =====
> 
> 
> On Tue, Feb 7, 2012 at 10:32 AM, Nathan Folkman <nate@path.com> wrote:
> Thanks for the offer to help. I'm quite familiar with R-trees, and already have some code that performs neighborhood lookups. ;) What would be great are pointers to specific open-source polygons, as finding all the data seems to be the time consuming part of all of this. 
> 
> - nrf
> 
> 
> On Feb 7, 2012, at 10:26 AM, Ben Standefer wrote:
> 
>> Nathan,
>> 
>> The primary data structure we use to performing a location lookup is an R-tree.  A ready-to-roll implementation of an R-tree is in PyPI (http://pypi.python.org/pypi/Rtree/).  It's really pretty simple to use, assuming you know the location of some good open-source polygons.
>> 
>> I'd be more than happy to sit down for a few hours for free on a weeknight or weekend to help explain what I know about how an R-tree works and how you could roll your own location lookup service without too much of a headache.  I can also show you some good free sources for polygon location data (city, state, zip, neighborhoods, etc.) and show you how to index that data into an R-tree.
>> 
>> A lot of the stuff that may seem like magic or intellecual property is just a little spatial know-how.  While we can't continue to provide the Context service or it's implementation details, I'd be more than happy to talk shop and give you a run down on how to perform spatial indexing of polygons into an R-tree.
>> 
>> I am available Wednesday night, Thursday night, and Sunday afternoon and evening.
>> 
>> -Ben
>> 
>> 
>> On Tue, Feb 7, 2012 at 8:53 AM, Nathan Folkman <nate@path.com> wrote:
>> Understand, thanks for the update. 
>> 
>> Sent from my iPhone
>> 
>> On Feb 7, 2012, at 8:45 AM, Sasha Mace <sasha@urbanairship.com> wrote:
>> 
>>> Unfortunately no, the service is too complex and intertwined across multiple Amazon AZ's and locations for us to support a remote installation on.  It is not designed to be installed on a per client basis. The monthly costs run in the multiple tens of thousands per month for maintaining the service beyond the 31st, and is an added burden on our team as well since we're removing this product from the market completely. Keeping it available beyond the end of Q1 is not feasible for Urban Airship.
>>> 
>>> Ben and I stand ready to help you stand up an alternative or migrate to other similar services however we can.
>>> 
>>> Yours,
>>> 
>>> Sasha Mace
>>> Director of Products
>>> Urban Airship, Inc.
>>> c: 503-702-5840
>>> 
>>> 
>>> On Feb 7, 2012, at 8:38 AM, Nathan Folkman wrote:
>>> 
>>>> Are there any options for us to host the service on our end?
>>>> 
>>>> Sent from my iPhone
>>>> 
>>>> On Feb 6, 2012, at 6:21 PM, Matt Van Horn <mvanhorn@path.com> wrote:
>>>> 
>>>>> Is there any way we can cover that cost to extend?
>>>>> 
>>>>> Sent from my iPhone
>>>>> 
>>>>> On Feb 6, 2012, at 5:56 PM, Sasha Mace <sasha@urbanairship.com> wrote:
>>>>> 
>>>>>> Matt,
>>>>>> 
>>>>>> Unfortunately I don't think we can accommodate an extension of the service beyond March 31st. We're not supporting this product line for any customers, and it has substantial monthly costs and overheard to maintain that make it unfeasible to leave it available.
>>>>>> 
>>>>>> I realize this adds a constraint for your development and migration. Please do let Ben and I know if there's anything we can help do to speed that up for you.
>>>>>> 
>>>>>> Yours,
>>>>>> 
>>>>>> Sasha Mace
>>>>>> Director of Products
>>>>>> Urban Airship, Inc.
>>>>>> c: 503-702-5840
>>>>>> 
>>>>>> 
>>>>>> On Feb 3, 2012, at 12:48 PM, Matt Van Horn wrote:
>>>>>> 
>>>>>>> Sasha and Ben,
>>>>>>> 
>>>>>>> Thanks for the advice and call.  We are working towards figuring out our solution 
>>>>>>> 
>>>>>>> Is there any way we can continue to use our SimpleGeo API's through the end of May?
>>>>>>> 
>>>>>>> We would really appreciate it, it would be a huge help to us as we work on our solution.
>>>>>>> 
>>>>>>> Thank you so much.  Call me if you would like to connect.  520-907-6052
>>>>>>> 
>>>>>>> vh
>>>>>>> 
>>>>>>> On Wed, Jan 11, 2012 at 1:36 PM, Sasha Mace <sasha@urbanairship.com> wrote:
>>>>>>> Matt,
>>>>>>> 
>>>>>>> Here is some migration information, ahead of our call next week. Talk to you on Tuesday.
>>>>>>> 
>>>>>>> SimpleGeo Context Alternatives
>>>>>>> The Google Geocoding API returns latitude and longitude data similar to SimpleGeo Context, including neighborhood, political boundaries, city, state, intersections, and even parks and airports. PlaceIQ provides a product called Place Context that returns intelligence about a specific place.
>>>>>>> 
>>>>>>> If you'd like to roll your own point-in-polygon lookup service, use an R-tree. Early prototypes of SimpleGeo Context use the Rtree Python package, which is pretty reliable because it's built on libspatialindex. You should be able to load polygons into an R-tree and perform point-in-polygon lookups.
>>>>>>> 
>>>>>>> We used many datasources to populate SimpleGeo Context. We used the US Census Bureau TIGER/Line dataset for roads, census tracts, voting districts, and demographics data. Natural Earth data was used for for countries, international provinces, and parks. Much of the hyper-local data such as intersections, stadiums, city parks, and buildings came from the amazing OpenStreetMap project (use Osmium to wrangle the data). Columbia University's SEDAC provides easy-to-use population density data.
>>>>>>> 
>>>>>>> Weather Decision Technologies is one of the leading providers of professional-level weather data, including forecasts, current conditions, temperatures, and much more. They are true weather geeks, provide professional-level support, and should cover all your high-end needs. Ready-to-use APIs that allow you to query weather by location include WeatherBug API, The Weather Channel API, and Weather Underground API.
>>>>>>> 
>>>>>>> SimpleGeo Storage Alternatives
>>>>>>> 
>>>>>>> Here's several suggestions for hosted spatial storage. Mobile backend startups StackMob and Parse allow you to specify latitudes and longitudes along with objects (we haven't evaluated either company's ability to scale). Google Fusion Tables and GeoCommons can store spatially-enabled data for analysis (transactional properties unknown). Oracle Spatial and Esri ArcGIS are products that let you store and do a lot with spatial data.
>>>>>>> 
>>>>>>> The best DIY-hosted spatial storage solution we can recommend is PostGIS, a spatial extension for the PostgreSQL database. You can get PostGIS functional in less than a day if you follow the GeoDjango tutorial and pay close attention to the PostGIS manual.
>>>>>>> 
>>>>>>> SimpleGeo Places Alternatives
>>>>>>> 
>>>>>>> We highly recommend using Factual for places data. The SimpleGeo Places data was supplied by Factual. Transition to Factual will be straightforward--simply map your existing SimpleGeo data in their Crosswalk API. You'll also be able to query the Factual API in similar ways you were able to query SimpleGeo Places.
>>>>>>> 
>>>>>>> Geocoding/Reverse Geocoding
>>>>>>> 
>>>>>>> Geocoding is the process of converting a street address to a latitude and longitude.  Reverse geocoding is the process of converting a latitude and longitude to a street address. International data collection and cultural differences make can make it tricky to geocode international addresses. Because the process is tricky, you do get what you pay for when it comes to geocoding. Most providers of geocoders also provide reverse geocoding capabilities.
>>>>>>> 
>>>>>>> Replacing the SimpleGeo Geocoder - SimpleGeo ran the open-source GeoCommons geocoder. It was originally written by SimpleGeo cartographer Schuyler Erle for GeoCommons. It is implemented in Ruby and SQLite. Because it uses freely-available US Census Bureau TIGER/Line street data, it can only geocode US addresses, and does not perform reverse geocodes. This geocoder is free, and the code can be forked on GitHub.
>>>>>>> 
>>>>>>> Using Professional Geocoding Services - NAVTEQ Web Services and Tele Atlas may require extra initial effort to get going, but they provide great results.
>>>>>>> 
>>>>>>> Using 'the Big Guys' - Google Geocoding API, Yahoo! PlaceFinder, and Bing Maps Locations API all provide some free geocoding as long as you stay within their respective Terms Of Service.
>>>>>>> 
>>>>>>> Yours,
>>>>>>> 
>>>>>>> Sasha Mace
>>>>>>> Director of Products
>>>>>>> Urban Airship, Inc.
>>>>>>> c: 503-702-5840
>>>>>>> 
>>>>>>> 
>>>>>>> On Jan 11, 2012, at 11:14 AM, Matt Van Horn wrote:
>>>>>>> 
>>>>>>>> Sounds good! Chat then!
>>>>>>>> 
>>>>>>>> What # shall I reach you at?
>>>>>>>> 
>>>>>>>> Sent from my iPhone
>>>>>>>> 
>>>>>>>> On Jan 11, 2012, at 8:42 AM, Sasha Mace <sasha@urbanairship.com> wrote:
>>>>>>>> 
>>>>>>>>> Matt,
>>>>>>>>> 
>>>>>>>>> Next Tuesday works, how about 2PM Pacific? I can send you our migration suggestions today for you to take a look at and we can go through it more in-depth next week.
>>>>>>>>> 
>>>>>>>>> Yours,
>>>>>>>>> 
>>>>>>>>> Sasha Mace
>>>>>>>>> Director of Products
>>>>>>>>> Urban Airship, Inc.
>>>>>>>>> c: 503-702-5840
>>>>>>>>> 
>>>>>>>>> 
>>>>>>>>> On Jan 11, 2012, at 8:02 AM, Matt Van Horn wrote:
>>>>>>>>> 
>>>>>>>>>> Thank you, Scott!
>>>>>>>>>> 
>>>>>>>>>> Sasha - Call next Tues afternoon?
>>>>>>>>>> 
>>>>>>>>>> Cheers,
>>>>>>>>>> Matt
>>>>>>>>>> 
>>>>>>>>>> On Wed, Jan 11, 2012 at 8:00 AM, Scott Kveton <scott@urbanairship.com> wrote:
>>>>>>>>>> Hey Guys,
>>>>>>>>>> 
>>>>>>>>>> I'm copying Sasha from here at UA ... he can talk to you about our
>>>>>>>>>> plans on this end as well as potential migration paths off for what
>>>>>>>>>> you guys are using so that you still get the functionality you need.
>>>>>>>>>> 
>>>>>>>>>> - Scott
>>>>>>>>>> 
>>>>>>>>>> 
>>>>>>>>>> 
>>>>>>>>>> On Mon, Jan 9, 2012 at 5:59 PM, Dave Morin <dave@path.com> wrote:
>>>>>>>>>> > Matt is the man
>>>>>>>>>> >
>>>>>>>>>> > On Jan 9, 2012, at 9:42 AM, Scott Kveton <scott@urbanairship.com> wrote:
>>>>>>>>>> >
>>>>>>>>>> >> We've got some ideas on this front ... do you or the right person on
>>>>>>>>>> >> your team have time for a call later this afternoon?
>>>>>>>>>> >>
>>>>>>>>>> >> Let me know,
>>>>>>>>>> >>
>>>>>>>>>> >> - Scott
>>>>>>>>>> >>
>>>>>>>>>> >>
>>>>>>>>>> >>
>>>>>>>>>> >> On Fri, Jan 6, 2012 at 3:37 PM, Dave Morin <dave@path.com> wrote:
>>>>>>>>>> >>> Thanks man. I can't tell you how important this is to us strategically�..
>>>>>>>>>> >>>
>>>>>>>>>> >>> ---Dave Morin / Co-Founder and CEO / Path
>>>>>>>>>> >>>
>>>>>>>>>> >>>
>>>>>>>>>> >>> On Friday, January 6, 2012 at 3:35 PM, Scott Kveton wrote:
>>>>>>>>>> >>>
>>>>>>>>>> >>>> Possibly ... let me talk with the guys here and see what it looks like
>>>>>>>>>> >>>> from a complexity standpoint. Will get back to you early next week.
>>>>>>>>>> >>>> We'll make something happen for you guys.
>>>>>>>>>> >>>>
>>>>>>>>>> >>>>
>>>>>>>>>> >>>>
>>>>>>>>>> >>>> On Fri, Jan 6, 2012 at 3:27 PM, Dave Morin <dave@path.com (mailto:dave@path.com)> wrote:
>>>>>>>>>> >>>>> Scott,
>>>>>>>>>> >>>>>
>>>>>>>>>> >>>>> We use the Context API for Reverse Geocoding and Weather. Your guys told my
>>>>>>>>>> >>>>> guys that you guys will be sunsetting it in the next couple of weeks.
>>>>>>>>>> >>>>>
>>>>>>>>>> >>>>> Is it possible for us to buy it from you so we can run it locally? It is
>>>>>>>>>> >>>>> incredibly important to our business.
>>>>>>>>>> >>>>>
>>>>>>>>>> >>>>> Dave
>>>>>>>>>> >>>>>
>>>>>>>>>> >>>>> --
>>>>>>>>>> >>>>> Dave Morin / Co-Founder and CEO / Path
>>>>>>>>>> >>>>
>>>>>>>>>> >>>
>>>>>>>>>> >>>
>>>>>>>>>> >>>
>>>>>>>>>> 
>>>>>>>>>> 
>>>>>>>>>> 
>>>>>>>>>> -- 
>>>>>>>>>> Matt Van Horn | Path | mvanhorn@path.com
>>>>>>>>>> Follow me on Twitter: http://twitter.com/mvanhorn
>>>>>>>>>> 
>>>>>>>>> 
>>>>>>> 
>>>>>>> 
>>>>>>> 
>>>>>>> 
>>>>>>> -- 
>>>>>>> Matt Van Horn | Path | mvanhorn@path.com
>>>>>>> Follow me on Twitter: http://twitter.com/mvanhorn
>>>>>>> 
>>>>>> 
>>> 
>> 
> 
> 

