from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

import foundation

urlpatterns = patterns('',
    url(
    	r'^$',
    	TemplateView.as_view(template_name="home.html"),
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
    url(
    	'',
    	include('social.apps.django_app.urls',
    		namespace='social'
    	)
    ),
    url(r'', include('user.urls', namespace='user')),
)
