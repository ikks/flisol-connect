#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext as _

from common.models import Country
from common.models import Distribution

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    list_display = (
        'name',
        'slug',
    )

    readonly_fields = [
        'created_at',
        'created_by',
    ]

    fieldsets = (
        (None, {
            'fields': (
                ('name', 'slug'),
                'description',
                ('logo_flag', 'image'),
            ),
        }),
        (_('Advanced'), {
            'fields': (
                ('map_center', 'map_zoom'),
                ('created_at', 'created_by'),
            ),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user

        super(
            CountryAdmin,
            self
        ).save_model(
            request,
            obj,
            form,
            change,
        )

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(CountryAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    list_display = (
        'name',
        'slug',
    )

    search_fields = (
        'name',
        'slug',
    )

    readonly_fields = (
        'created_at',
        'created_by',
    )

    fieldsets = (
        (None, {
            'fields': (
                ('name', 'slug'),
                'description',
                'logo', 'wikipedia',
            ),
        }),
        (_('Advanced'), {
            'fields': (
                ('created_at', 'created_by'),
            ),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user

        super(
            DistributionAdmin,
            self
        ).save_model(
            request,
            obj,
            form,
            change,
        )

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(DistributionAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions