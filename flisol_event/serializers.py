#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _

from common.models import Country
from flisol_event.models import FlisolAttendance
from flisol_event.models import FlisolInstance
from flisol_event.models import FlisolInstanceRequest
from flisol_event.models import FlisolMachine

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
        Create and return a new `FlisolInstance` instance.
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


class FlisolAttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlisolAttendance
        fields = (
            'id',
            'role',
            'flisol_instance',
            'user',
            'comment',
        )

    def validate(self, data):
        if FlisolAttendance.objects.filter(
            user=data['user'],
            flisol_instance=data['flisol_instance'],
        ).exists():
            raise serializers.ValidationError(
                _('You are allowed to subscribe just once')
            )


class FlisolMachineSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlisolMachine
        fields = (
            'id',
            'flisol_instance',
            'machine_type',
            'registar',
            'description',
        )

