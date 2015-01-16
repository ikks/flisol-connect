#! /usr/bin/env python
# -*- coding: utf-8 -*-
from crispy_forms_foundation.forms import FoundationModelForm
from django import forms
from django.utils.translation import ugettext as _

from flisol_event.models import FlisolInstance
from flisol_event.models import FlisolAttendance
from flisol_event.models import FlisolMachine
from flisol_event.models import FlisolInstanceRequest

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout


class FlisolInstanceRequestForm(FoundationModelForm):

    class Meta:
        model = FlisolInstanceRequest
        fields = (
            'map_center',
            'country',
            'city_name',
            'description',
        )

        widgets = {
            'map_center': forms.HiddenInput,
            'country': forms.HiddenInput,
        }

    def _init_(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'city_name',
            'description',
        )
        super(FlisolInstanceRequestForm, self).__init__(*args, **kwargs)


class FlisolInstanceForm(FoundationModelForm):

    iso_code = forms.CharField(
        label='',
        max_length=3,
        widget=forms.HiddenInput
    )

    class Meta:
        model = FlisolInstance
        fields = (
            'city_name',
            'instance_name',
            'description',
            'address',
            'schedule',
            'map_center',
            'map_zoom',
        )

        widgets = {
            'map_center': forms.HiddenInput,
            'map_zoom': forms.HiddenInput,
        }

    def _init_(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'city_name',
            'instance_name',
            'address',
            'description',
        )
        super(FlisolInstanceRequestForm, self).__init__(*args, **kwargs)


class FlisolAttendanceForm(FoundationModelForm):

    has_machine = forms.BooleanField(
        label=_('I have a machine to be migrated!!!!!'),
        initial=True,
    )

    class Meta:
        model = FlisolAttendance
        fields = (
            'role',
            'comment',
            'flisol_instance',
        )
        widgets = {
            'flisol_instance': forms.HiddenInput,
        }


class FlisolMachineForm(FoundationModelForm):

    class Meta:
        model = FlisolMachine
        fields = (
            'machine_type',
            'requested_distro',
            'description',
            'flisol_instance'
        )

        widgets = {
            'flisol_instance': forms.HiddenInput,
        }
