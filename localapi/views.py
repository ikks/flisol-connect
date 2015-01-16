#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.cache import cache

from flisol_event.models import FlisolAttendance
from flisol_event.models import FlisolInstance
from flisol_event.models import FlisolInstanceRequest
from flisol_event.serializers import FlisolAttendanceSerializer
from flisol_event.serializers import FlisolInstanceRequestSerializer
from flisol_event.serializers import FlisolInstanceSerializer
from flisol_event.serializers import FlisolMachineSerializer

from constance import config
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class FlisolInstanceList(generics.ListCreateAPIView):
    queryset = FlisolInstance.objects.all()
    serializer_class = FlisolInstanceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('city_name', 'instance_name', 'slug')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        instance = serializer.save(
            created_by=self.request.user,
            flisol_event_id=config.CURRENT_FLISOL_ID,
        )
        if not FlisolAttendance.objects.filter(
            flisol_instance__id=config.CURRENT_FLISOL_ID,
            user=self.request.user,
        ).exists():
            FlisolAttendance.objects.create(
                role=FlisolAttendance.ATTENDANCE_CHOICES_OTHER,
                flisol_instance=instance,
                user=self.request.user,
                can_update=True,
                comment=u'Creador de la instancia'
            )


class FlisolInstanceRequestList(generics.ListCreateAPIView):
    queryset = FlisolInstanceRequest.objects.all()
    serializer_class = FlisolInstanceRequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            flisol_event_id=config.CURRENT_FLISOL_ID,
        )

    def get_queryset(self):
        queryset = super(FlisolInstanceRequestList, self).get_queryset()
        if self.request.user.is_staff == True:
            return queryset
        if self.request.user.is_authenticated():
            queryset = queryset.filter(created_by=self.request.user)
        return queryset


class FlisolSubscriptionCreation(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, format=None):
        data = dict(request.data.items())
        data['user'] = request.user.id
        att_serializer = FlisolAttendanceSerializer(data=data)
        if att_serializer.is_valid():
            attendance = att_serializer.save()
        else:
            data['errors'] = att_serializer.errors

        if attendance.role == attendance.ATTENDANCE_CHOICES_VISITOR:
            data['registar'] = request.user.id
            comment = data.pop('comment')
            mac_serializer = FlisolMachineSerializer(data=data)
            if mac_serializer.is_valid():
                machine = mac_serializer.save()
            data['comment'] = comment

        return Response(data)

