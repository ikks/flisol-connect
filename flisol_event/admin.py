#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext as _

from flisol_event.models import FlisolInstance


@admin.register(FlisolInstance)
class FlisolInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'city_name',
        'instance_name',
        'slug',
        'status',
        'email_contact',
        'wiki_url',
    )

    search_fields = (
        'city_name',
        'instance_name',
        'slug',
    )

    list_filter = (
        'status',
        'country',
    )

    readonly_fields = [
        'created_at',
    ]

    fieldsets = (
        (None, {
            'fields': (
                'flisol_event',
                ('city_name', 'instance_name'),
                ('country', 'status'),
                ('map_center', 'map_zoom'),
            ),
        }),
        (_('additional'), {
            'fields': (
                ('address', 'schedule'),
                'description',
                'image',
                ('email_contact', 'wiki_url'),
                ('created_at', 'created_by'),
            ),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        # make all fields readonly
        read_only_fields = list(set(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]
        ))
        return read_only_fields

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
