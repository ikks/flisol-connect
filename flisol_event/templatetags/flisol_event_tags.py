#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
from django.core.cache import cache

from flisol_event.forms import FlisolInstanceForm
from flisol_event.forms import FlisolInstanceRequestForm
from flisol_event.forms import FlisolAttendanceForm
from flisol_event.models import FlisolAttendance
from flisol_event.forms import FlisolMachineForm

register = template.Library()


@register.inclusion_tag('flisol_event/_main_forms.html')
def basic_forms():
    return {
        'request_form': FlisolInstanceRequestForm(prefix='request'),
        'creation_form': FlisolInstanceForm(prefix='instance'),
        'subscription_form': FlisolAttendanceForm(prefix='subscription'),
        'machine_form': FlisolMachineForm(prefix='machine'),
        'visitor_id': FlisolAttendance.ATTENDANCE_CHOICES_VISITOR
    }
