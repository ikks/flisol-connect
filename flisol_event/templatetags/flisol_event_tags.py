#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
from django.core.cache import cache

from flisol_event.forms import FlisolInstanceForm
from flisol_event.forms import FlisolInstanceRequestForm

register = template.Library()


@register.inclusion_tag('flisol_event/_main_forms.html')
def basic_forms():
    return {
        'request_form': FlisolInstanceRequestForm,
        'creation_form': FlisolInstanceForm,
        'subscription_form': '',
    }