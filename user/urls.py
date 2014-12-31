#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls import patterns
from django.core.urlresolvers import reverse_lazy

from user.forms import CustomAuthenticationForm
from user.forms import CustomPasswordResetForm
from user.forms import CustomSetPasswordForm
from user.views import UserDetailView
from user.views import UserRegistrationView
from user.views import UserUpdateView


urlpatterns = patterns(
    '',

    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        {
            'authentication_form': CustomAuthenticationForm,
        },
        name='login',
    ),

    url(r'^usuario/$', UserDetailView.as_view(), name='me'),

    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        {
            'next_page': reverse_lazy('home'),
        },
        name='logout',
    ),


    url(
        r'^password/reset/$',
        'django.contrib.auth.views.password_reset',
        {
            'post_reset_redirect':
            reverse_lazy('user:password_reset_done'),
            'password_reset_form': CustomPasswordResetForm,
        },
        name='password_reset',
    ),
    url(
        r'^password/reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        name='password_reset_done',
    ),
    url(
        r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {
            'post_reset_redirect':
            reverse_lazy('user:password_reset_complete'),
            'set_password_form': CustomSetPasswordForm,
        },
        name='password_reset_confirm',
    ),
    url(
        r'^password/done/$',
        'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete',
    ),

    url(
        r'^suscribirse/$',
        UserRegistrationView.as_view(),
        name='registration',
    ),

    url(
        r'^actualizar/$',
        UserUpdateView.as_view(),
        name='profile_update',
    ),

)
