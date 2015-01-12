#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model

from flisol_event.models import FlisolInstance
from flisol_event.models import FlisolInstanceRequest

from rest_framework import serializers
from rest_framework.reverse import reverse


class FlisolInstanceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FlisolInstance
        fields = (
            'city_name',
            'instance_name',
            'description',
            'address',
            'schedule',
            'map_center',
            'map_zoom',
            'country',
        )


class FlisolInstanceRequestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FlisolInstanceRequest
        fields = (
            'map_center',
            'country',
            'city_name',
            'description',
        )
