
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>reverse geo</title>
    <meta name="description" content="">
    <meta name="author" content="">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />

    <!-- Le HTML5 shim, for IE6-8 support of HTML elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Le styles -->
    <link href="/static/bootstrap/css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
      #map_canvas img { max-width:none; }
    </style>
    <link href="/static/bootstrap/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- Le fav and touch icons -->
    <link rel="shortcut icon" href="/static/favicon.ico">


    <script type="text/javascript"
      src="http://maps.googleapis.com/maps/api/js?key=AIzaSyADuPn6J0sWQuKLu1zvn0d1tcgnEi5uVO4&sensor=false">
    </script>
    <script type="text/javascript">
var map;
var results = {}
function initialize() {
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(38.8951118, -77.0363658)
    var myOptions = {
      zoom: 8,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP,
      zoomControl: true,
      zoomControlOptions: {
        style: google.maps.ZoomControlStyle.LARGE
      },
    }
    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
    google.maps.event.addListener(map, 'click', function(event) {
      on_click(event.latLng);
    });
    codeAddress()
}

function codeAddress() {
    var address = document.getElementById("address").value;
    geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        console.log(results[0].geometry.location)
        map.setCenter(results[0].geometry.location);
        var marker = new google.maps.Marker({
            map: map,
            position: results[0].geometry.location
        });
      } else {
        alert("Geocode was not successful for the following reason: " + status);
      }
    });
}

function draw_bbox(o) {
    // our bbox is  (left, bottom, right, top)
    var coords = [
         new google.maps.LatLng(o.bbox[3], o.bbox[2]),
         new google.maps.LatLng(o.bbox[3], o.bbox[0]),
         new google.maps.LatLng(o.bbox[1], o.bbox[0]),
         new google.maps.LatLng(o.bbox[1], o.bbox[2]),
    ]
    console.log(coords)
    bbox = new google.maps.Polygon({
        paths: coords,
        strokeColor: "#FF0000",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#FF0000",
        fillOpacity: 0.35
    });

    bbox.setMap(map);
}

function on_click(location) {
    lat = location.lat()
    lng = location.lng()
    console.log(lat, lng)
    $.ajax({
      url: '/geo',
      dataType: 'json',
      data: {lat:lat, lng:lng},
      success: function(o) {
          html = '<h1>Places</h1><ul>'
          for (var i in o.data) {
              el = o.data[i]
              results[el.name] = el
              console.log(el)
              props=[]
              for(var k in el.properties) {
                  props.push(k+"="+el.properties[k])
              }
              html += '<li><a href="#">'+el.name+'</a> '+props.join(', ')+'</li>'
          }
          html += '</ul>'
          $('div.places').html(html)
          $('div.places a').click(function(){
              console.log($(this))
              var name = $(this).text()
              draw_bbox(results[name])
              return false;
          })
      }
    });
}

    </script>

  </head>

  <body onload="initialize()">

    <img src="http://maps.gstatic.com/mapfiles/openhand_8_8.cur" style="visibility:hidden"/>
    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="#">Jay Ridgeway</a>
          <div class="nav-collapse">
            <ul class="nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="#about">About</a></li>
              <li><a href="#contact">Contact</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">

      <h1>Reverse Geo <small>click to select a location</small></h1>
      <div id="map_canvas" style="width:940px; height:450px"></div>
      <div>
        <form onsubmit="codeAddress();return false;">
        <input id="address" type="textbox" value="San Francisco, CA">
        <input type="button" value="Jump" onclick="codeAddress()">
        </form>

      </div>
      <div class="places">
      </div>


    </div> <!-- /container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
    <script src="/static/bootstrap/js/bootstrap.min.js"></script>

  </body>
</html>

