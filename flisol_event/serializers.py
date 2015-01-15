#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model

from common.models import Country
from flisol_event.models import FlisolInstance
from flisol_event.models import FlisolInstanceRequest

from rest_framework import serializers
from rest_framework.reverse import reverse


class FlisolInstanceSerializer(serializers.ModelSerializer):

    iso_code = serializers.CharField()

    class Meta:
        model = FlisolInstance
        fields = (
            'id',
            'city_name',
            'instance_name',
            'description',
            'address',
            'schedule',
            'map_center',
            'map_zoom',
            'iso_code',
        )

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        country = Country.objects.get(iso_code=validated_data['iso_code'])
        del validated_data['iso_code']
        validated_data['country'] = country
        instance = FlisolInstance.objects.create(**validated_data)
        return instance


class FlisolInstanceRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlisolInstanceRequest
        fields = (
            'map_center',
            'country',
            'city_name',
            'description',
        )
