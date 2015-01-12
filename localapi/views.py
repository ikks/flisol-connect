#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.cache import cache

from flisol_event.models import FlisolInstance
from flisol_event.models import FlisolInstanceRequest
from flisol_event.serializers import FlisolInstanceSerializer
from flisol_event.serializers import FlisolInstanceRequestSerializer

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from rest_framework import permissions


class FlisolInstanceList(generics.ListCreateAPIView):
    queryset = FlisolInstance.objects.all()
    serializer_class = FlisolInstanceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('city_name', 'instance_name', 'slug')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            flisol_event_id=cache.get('current_event_id'),
        )

class FlisolInstanceRequestList(generics.ListCreateAPIView):
    queryset = FlisolInstanceRequest.objects.all()
    serializer_class = FlisolInstanceRequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            flisol_event_id=cache.get('current_event_id'),
        )

    def get_queryset(self):
        queryset = super(FlisolInstanceRequestList, self).get_queryset()
        if self.request.user.is_superuser == True:
            return queryset
        queryset = queryset.filter(created_by=self.request.user)
