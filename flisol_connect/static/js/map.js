var map;
var feature;

function load_map() {
    map = new L.Map('map', {zoomControl: true, scrollWheelZoom: false});

    var osmUrl = 'https://{s}.tiles.mapbox.com/v3/examples.3hqcl3di/{z}/{x}/{y}.png',
        osmAttribution = 'Datos de <a href="http://openstreetmap.org/">OpenStreetMap</a>, tiles cortesía de mapbox.',
        osm = new L.TileLayer(osmUrl, {maxZoom: 13, attribution: osmAttribution});

    map.setView(new L.LatLng(-8 , -70), 3).addLayer(osm);
    $.get($('.url-instances').data('url-instance-list'), function(result){
        var template = Handlebars.compile($('#instance-popup-template').html());
        for (var i=0; i < result.length; i++){
            var content = result[i];
            content['label_subscribe'] = $('#instance-list').data('label-subscribe');
            content['help_subscribe'] = $('#instance-list').data('help-subscribe');
            L.marker(result[i].map_center.split(',')).addTo(map).bindPopup(template(content));
        }
        $(document).foundation();
        $(document).foundation('reveal', 'reflow');

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
        var items = [];

        $.each(data, function(key, val) {
            var name = val.display_name.split(',')[0];
            var country = val.address.country_code;
            var lon = val.lon;
            var lat = val.lat;
            var bb = val.boundingbox;
            items.push({
                'name': name,
                'country': country,
                'lon': lon,
                'lat': lat,
                'bb0': bb[0],
                'bb2': bb[2],
                'bb1': bb[1],
                'bb3': bb[3],
                'osm_type': val.osm_type,
                'display_name': val.display_name,
            });
        });
        var data = {
            'places': items,
            'label_create': $('#place-list').data('label-create'),
            'help_create': $('#place-list').data('help-create'),
            'label_request': $('#place-list').data('label-request'),
            'help_request': $('#place-list').data('help-request'),
        }
        var template = Handlebars.compile($('#result-template').html());
        $('#place-list').empty().html(template(data));
        $(document).foundation();
        $(document).foundation('reveal', 'reflow');
        $('#search').foundation('reveal', 'open');
        inp.val('');
    });
    return false;
}

function look_for_flisol() {
    $.get($('#search').data('flisol-search-url') + '?search=' + $("#flisol-place").val(),
        function(result){
            $('#instance-list').empty();
            if (result.length > 0) {
                var template = Handlebars.compile($('#instance-list-template').html());
                var data = {
                    'places': result,
                    'label_subscribe': $('#instance-list').data('label-subscribe'),
                    'help_subscribe': $('#instance-list').data('help-subscribe'),
                }
                $('#instance-list').html(template(data));
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
    if ($('#map').length === 0)
        return;
    load_map();
    $('.searchplace').on('submit',look_for_flisol);
    $('#addr').on('click',look_for_flisol);
    $('#place-list').on('click', '.js-request-instance', function(){
        $('#id_request-map_center').val(
            $(this).closest('.data-info').data('lat') + ',' +
            $(this).closest('.data-info').data('lon')
        );
        $('#id_request-country').val($(this).closest('.data-info').data('country-code'));
        $('#id_request-city_name').val($(this).closest('.data-info').data('name'));
        $('#instance-request').foundation('reveal', 'open');
    });
    $('#place-list').on('click', '.js-create-instance', function(){
        $('#id_instance-map_center').val(
            $(this).closest('.data-info').data('lat') + ',' +
            $(this).closest('.data-info').data('lon')
        );
        $('#id_instance-iso_code').val($(this).closest('.data-info').data('country-code'));
        $('#id_instance-city_name').val($(this).closest('.data-info').data('name'));
        $('#instance-creation').foundation('reveal', 'open');
    });
    $(document).on('click', '.js-preview-instance', function(){
        var info = $(this).closest('.data-info');
        point = info.data('map-center').split(',');
        zoom = info.data('map-zoom');
        map.setView(point, zoom);
    });
    $(document).on('click', '.js-subscribe', function(){
        var info = $(this).closest('.data-info');
        $('#id_machine-flisol_instance').val(info.data('instance-id'));
        $('.instance-name').html(info.data('instance-name'));
        map.closePopup();
        $('#div_id_subscription-comment').hide();
        $('#instance-subscription').foundation('reveal', 'open');
    });
    $('#place-list').on('click', '.js-zoomto', function(){
        var item = $(this);
        chooseAddr(item.data('l1'), item.data('l2'), item.data('l3'), item.data('l4'), item.data('type-node'))
    });
    $('#id_subscription-role').on('change', function(){
        if ($('#id_subscription-role').val() === $('.subscription-form').data('visitor-id').toString()) {
            $('#div_id_subscription-has_machine').show();
            if ($('#id_subscription-has_machine').is(":checked")) {
                $('#div_id_machine-machine_type,#div_id_machine-requested_distro,#div_id_machine-description').show();
            }
            else {
                $('#div_id_machine-machine_type,#div_id_machine-requested_distro,#div_id_machine-description').hide();
            }
            $('#div_id_subscription-comment').hide();
        }
        else {
            $('#div_id_subscription-has_machine,#div_id_machine-machine_type,#div_id_machine-requested_distro,#div_id_machine-description').hide();
            $('#div_id_subscription-comment').show();
        }
    });
    $('#id_subscription-has_machine').on('change', function() {
        if ($('#id_subscription-has_machine').is(":checked")) {
                $('#div_id_machine-machine_type,#div_id_machine-requested_distro,#div_id_machine-description').show();
            }
            else {
                $('#div_id_machine-machine_type,#div_id_machine-requested_distro,#div_id_machine-description').hide();
            }
    });

    $('.js-form').on('submit', function () {
        var the_form = $(this)
        $.post($(this).attr('action'), replaceall($(this).serialize(), $(this).data('prefix') , ''), function(result){
            $(".alert-content").html('<p>Operación exitosa').show();
            $('.reveal-modal').foundation('reveal', 'close');
        });
        return false;
    });
});
