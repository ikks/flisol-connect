var map;
var feature;

function load_map() {
    map = new L.Map('map', {zoomControl: true, scrollWheelZoom: false});

    var osmUrl = 'https://{s}.tiles.mapbox.com/v3/examples.3hqcl3di/{z}/{x}/{y}.png',
        osmAttribution = 'Datos de <a href="http://openstreetmap.org/">OpenStreetMap</a>, tiles cortesía de mapbox.',
        osm = new L.TileLayer(osmUrl, {maxZoom: 13, attribution: osmAttribution});

    map.setView(new L.LatLng(-8 , -70), 3).addLayer(osm);
    $.get($('.url-instances').data('url-instance-list'), function(result){
        for (var i=0; i < result.length; i++){
            L.marker(result[i].map_center.split(',')).addTo(map).bindPopup(result[i].city_name);
        }
    });
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

    $.getJSON('http://nominatim.openstreetmap.org/search?format=json&viewbox=-115,81,-35,-56&addressdetails=1&bounded=1&limit=5&q=' + inp.val(), function(data) {
        var items = ['<li><a href="#" class="js-subscribe"><i class="step fi-ticket"></i></a>'];

        $.each(data, function(key, val) {
            var name = val.display_name.split(',')[0];
            var country = val.address.country_code;
            var lon = val.lon;
            var lat = val.lat;
            var bb = val.boundingbox;
            items.push('<li data-name="' + name + '" data-country-code="' + country + '" data-lon="' + lon + '" data-lat="' + lat + '"><a href="#" class="js-zoomto" data-l1="' + bb[0] + '" data-l2="' + bb[2] + '" data-l3="' + bb[1] + '" data-l4="' + bb[3]  + '" data-type-node="' + val.osm_type + '">' + val.display_name + '</a><a href="#" class="js-request-instance" alt="Solicitar" title="Solicitar"><i class="step fi-shopping-cart"></i></a><a href="#" class="js-create-instance" alt="Crear" title="Crear"><i class="step fi-star"></i></a></li>');
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

function look_for_flisol() {
    $.get($('#search').data('flisol-search-url') + '?q=' + $("#flisol-place").val(),
        function(result){
            if (result.length === 0) {
            }
            addr_search();
        }
    )
    return false;
}

function replaceall(original, to_replace, replacement) {
    re = new RegExp(to_replace, "g");
    return original.replace(re, replacement);
}

$(function() {
    load_map();
    $('.searchplace').on('submit',look_for_flisol);
    $('#addr').on('click',look_for_flisol);
    $('#results').on('click', '.js-request-instance', function(){
        $('#id_request-map_center').val(
            $(this).parent().data('lat') + ',' +
            $(this).parent().data('lon')
        );
        $('#id_request-country').val($(this).parent().data('country-code'));
        $('#id_request-city_name').val($(this).parent().data('name'));
        $('#instance-request').foundation('reveal', 'open');
    });
    $('#results').on('click', '.js-create-instance', function(){
        $('#id_instance-map_center').val(
            $(this).parent().data('lat') + ',' +
            $(this).parent().data('lon')
        );
        $('#id_instance-iso_code').val($(this).parent().data('country-code'));
        $('#id_instance-city_name').val($(this).parent().data('name'));
        $('#instance-creation').foundation('reveal', 'open');
    });
    $('#results').on('click', '.js-subscribe', function(){
        $('#div_id_subscription-comment').hide();
        $('#instance-subscription').foundation('reveal', 'open');
    });
    $('#results').on('click', '.js-zoomto', function(){
        var item = $(this);
        chooseAddr(item.data('l1'), item.data('l2'), item.data('l3'), item.data('l4'), item.data('type-node'))
    });
    $('#id_subscription-role').on('change', function(){
        if ($('#id_subscription-role').val() === $('.subscription-form').data('visitor-id').toString()) {
            $('#div_id_machine-machine_type,#div_id_machine-requested_distro,#div_id_machine-description').show();
            $('#div_id_subscription-comment').hide();
        }
        else {
            $('#div_id_machine-machine_type,#div_id_machine-requested_distro,#div_id_machine-description').hide();
            $('#div_id_subscription-comment').show();
        }
    });

    $('.js-form').on('submit', function () {
        $.post($(this).attr('action'), replaceall($(this).serialize(), $(this).data('prefix') , ''), function(result){
            $(".alert-content").html('<p>Operación exitosa').show();
        });
        return false;
    });
});
