var map;
var feature;

function load_map() {
    map = new L.Map('map', {zoomControl: true, scrollWheelZoom: false});

    var osmUrl = 'https://{s}.tiles.mapbox.com/v3/examples.3hqcl3di/{z}/{x}/{y}.png',
        osmAttribution = 'Datos de <a href="http://openstreetmap.org/">OpenStreetMap</a>, tiles cortesía de mapbox.',
        osm = new L.TileLayer(osmUrl, {maxZoom: 13, attribution: osmAttribution});

    map.setView(new L.LatLng(-8 , -70), 3).addLayer(osm);
     L.marker([2.939, -75.29455]).addTo(map).bindPopup('Neiva, 23 de Abril de 2.015');
     L.marker([-22.9209, -43.25151]).addTo(map).bindPopup('Río de Janeiro, 24 de Abril de 2.015');
     L.marker([20.37778, -76.6444]).addTo(map).bindPopup('Bayamo, 24 de Abril de 2.015');
}

function chooseAddr(lat1, lng1, lat2, lng2, osm_type) {
    var loc1 = new L.LatLng(lat1, lng1);
    var loc2 = new L.LatLng(lat2, lng2);
    var bounds = new L.LatLngBounds(loc1, loc2);

    if (feature) {
        map.removeLayer(feature);
    }
    if (osm_type == "node") {
        feature = L.circle( loc1, 50, {color: 'red', fill: false}).addTo(map);
        map.fitBounds(bounds);
        map.setZoom(18);
    } else {
        var loc3 = new L.LatLng(lat1, lng2);
        var loc4 = new L.LatLng(lat2, lng1);

        feature = L.polyline( [loc1, loc4, loc2, loc3, loc1], {color: 'red'}).addTo(map);
        map.fitBounds(bounds);
    }
}

function addr_search() {
    var inp = $("#flisol-place");

    $.getJSON('http://nominatim.openstreetmap.org/search?format=json&viewbox=-115,81,-35,-56bounded=1&limit=5&q=' + inp.val(), function(data) {
        var items = [];

        $.each(data, function(key, val) {
            bb = val.boundingbox;
            items.push("<li><a href='#' onclick='chooseAddr(" + bb[0] + ", " + bb[2] + ", " + bb[1] + ", " + bb[3]  + ", \"" + val.osm_type + "\");return false;'>" + val.display_name + '</a></li>');
        });

        $('#results').empty();
        if (items.length != 0) {
            $('<h1>', { html: "Algunos sitios que coinciden:" }).appendTo('#results');
            $('<ul/>', {
                'class': 'my-new-list',
                html: items.join('')
            }).appendTo('#results');
        } else {
            $('<p>', { html: "No encontramos nada" }).appendTo('#results');
        }
        $('#search').foundation('reveal', 'open');
        inp.val('');
    });
    return false;
}

$(function() {
    load_map();
});
