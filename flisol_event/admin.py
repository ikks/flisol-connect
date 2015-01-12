#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext as _

from flisol_event.models import FlisolEvent
from flisol_event.models import FlisolInstance
from flisol_event.models import FlisolInstanceRequest
from flisol_event.models import FlisolMachine


@admin.register(FlisolEvent)
class FlisolEventAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}

    list_display = (
        'name',
        'slug',
        'official_date',
    )

    search_fields = (
        'name',
        'slug',
    )

    fieldsets = (
        (None, {
            'fields': (
                ('name', 'logo'),
                ('official_date', 'slug'),
                'description',
            ),
        }),
    )

    def save_model(self, request, obj, form, change):
        """Método sobreescrito para guardar automaticamente el creador
        """
        if not change:
            obj.created_by = request.user

        super(
            FlisolEventAdmin,
            self
        ).save_model(
            request,
            obj,
            form,
            change,
        )

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.prepopulated_fields = {}
            return self.readonly_fields + ('slug',)
        return self.readonly_fields


@admin.register(FlisolInstance)
class FlisolInstanceAdmin(admin.ModelAdmin):

    list_display = (
        'country',
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


@admin.register(FlisolInstanceRequest)
class FlisolInstanceRequestAdmin(admin.ModelAdmin):

    list_display = (
        'city_name',
        'country',
        'created_at',
        'created_by',
    )

    search_fields = (
        'city_name',
        'created_by__email',
        'country',
    )

    list_filter = (
        'flisol_event',
        'created_at',
    )

    fieldsets = (
        (None, {
            'fields': (
                ('country', 'city_name',),
                ('created_at', 'created_by'),
                'description',
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


@admin.register(FlisolMachine)
class FlisolMachineAdmin(admin.ModelAdmin):

    list_display = (
        'is_installed',
        'machine_type',
        'requested_distro',
        'installed_distro',
        'registar',
        'installed_by',
    )

    search_fields = (
        'installed_by__first_name',
        'installed_by__last_name',
        'installed_by__email',
        'registar__first_name',
        'registar__last_name',
        'registar__email',
    )

    list_filter = (
        'is_installed',
        'machine_type',
        'installed_distro',
        'requested_distro',
    )

    readonly_fields = [
        'created_at',
    ]

    fieldsets = (
        (None, {
            'fields': (
                ('machine_type', 'is_installed'),
                ('registar', 'installed_by'),
                ('requested_distro', 'installed_distro'),
                'description',
                ('installed_at', 'created_at'),
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
