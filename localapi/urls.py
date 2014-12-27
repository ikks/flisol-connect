#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AxiaCore S.A.S. http://axiacore.com
from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include

from localapi import views

from rest_framework.routers import SimpleRouter


# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register(r'flisol', views.FlisolInstanceSet)

urlpatterns = patterns(
    'localapi.views',
    # url(r'^$', 'api_root', name='api_root'),
    url(r'^', include(router.urls)),
)
