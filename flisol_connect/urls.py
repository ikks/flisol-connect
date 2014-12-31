#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from flisol_connect.views import HomePageView

import foundation


urlpatterns = patterns(
    '',
    url(
        r'^$',
        HomePageView.as_view(),
        name="home"
    ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^foundation/', include('foundation.urls')),
    url(
        r'^api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),

    # API
    url(
        r'^api/',
        include('localapi.urls', namespace='api')
    ),

    (r'^i18n/', include('django.conf.urls.i18n')),

    url(
        '',
        include(
            'social.apps.django_app.urls',
            namespace='social'
        )
    ),

    url(r'', include('user.urls', namespace='user')),

)
