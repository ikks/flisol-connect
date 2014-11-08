var map;
var feature;

function load_map() {
    map = new L.Map('map', {zoomControl: true});

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
        feature = L.circle( loc1, 25, {color: 'green', fill: false}).addTo(map);
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
    var inp = document.getElementById("addr");

    $.getJSON('http://nominatim.openstreetmap.org/search?format=json&-115,-56,-35,81&limit=5&q=' + inp.value, function(data) {
        var items = [];

        $.each(data, function(key, val) {
            bb = val.boundingbox;
            items.push("<li><a href='#' onclick='chooseAddr(" + bb[0] + ", " + bb[2] + ", " + bb[1] + ", " + bb[3]  + ", \"" + val.osm_type + "\");return false;'>" + val.display_name + '</a></li>');
        });

        $('#results').empty();
        if (items.length != 0) {
            $('<a style="cursor:hand;" class="js-clear-search">X</a>').appendTo('#results');
            $('<p>', { html: "Search results:" }).appendTo('#results');
            $('<ul/>', {
                'class': 'my-new-list',
                html: items.join('')
            }).appendTo('#results');
        } else {
            $('<p>', { html: "No results found" }).appendTo('#results');
        }
    });
}

$(function() {
    $('#search').on('click', '.js-clear-search', function(){
        $('#results').empty();
        $('#addr').val('');
    });
    $('#search').on('submit', 'form', function(){
        addr_search();
        return false;
    });
});
window.onload = load_map;
