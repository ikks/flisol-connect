#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com
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
            'address',
            'slug',
            'map_center',
            'map_zoom',
            'image',
            'status',
            'wiki_url',
            'instance_date',
        )


class FlisolInstanceRequestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FlisolInstanceRequest
        fields = (
            'city_name',
            'description',
        )
