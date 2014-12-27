#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com
from flisol_event.models import FlisolInstance
from flisol_event.serializers import FlisolInstanceSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters


class FlisolInstanceList(generics.ListAPIView):
    queryset = FlisolInstance.objects.all()
    serializer_class = FlisolInstanceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('city_name', 'instance_name', 'slug')
