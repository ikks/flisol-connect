#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com
from flisol_event.models import FlisolInstance
from flisol_event.serializers import FlisolInstanceSerializer
from rest_framework import viewsets


class FlisolInstanceSet(viewsets.ReadOnlyModelViewSet):
    queryset = FlisolInstance.objects.all()
    serializer_class = FlisolInstanceSerializer
