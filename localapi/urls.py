#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include

from localapi import views

from rest_framework.routers import SimpleRouter


urlpatterns = patterns(
    'localapi.views',
    url(
        r'^instancias/$',
        views.FlisolInstanceList.as_view(),
        name='instance',
    ),
    url(
        r'^solicitudes/$',
        views.FlisolInstanceRequestList.as_view(),
        name='request',
    ),
)
