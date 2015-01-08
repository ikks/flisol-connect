#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from crispy_forms_foundation.forms import FoundationModelForm

from flisol_event.models import FlisolInstance
from flisol_event.models import FlisolInstanceRequest

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout
from crispy_forms_foundation.layout import Submit
from crispy_forms_foundation.layout import ButtonHolder


class FlisolInstanceRequestForm(FoundationModelForm):

    class Meta:
        model = FlisolInstanceRequest
        fields = (
            'city_name',
            'description',
        )

    def _init_(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'city_name',
            'description',
            ButtonHolder(
                Submit('submit', _('Request'), css_class="button"),
            ),
        )
        super(FlisolInstanceRequestForm, self).__init__(*args, **kwargs)


class FlisolInstanceForm(FoundationModelForm):

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
            'wiki_url',
            'country',
        )

        widgets = {
            'map_center': forms.HiddenInput,
            'map_zoom': forms.HiddenInput,
            'country': forms.HiddenInput,
        }

    def _init_(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'city_name',
            'instance_name',
            'address',
            'description',
            ButtonHolder(
                Submit('submit', _('Create'), css_class="button"),
            ),
        )
        super(FlisolInstanceRequestForm, self).__init__(*args, **kwargs)

