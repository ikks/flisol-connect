#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()


class CustomUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(
        help_text=u'Puede <a href="password/">\
        cambiar la clave para este usuario</a>',
    )

    class Meta:
        model = User

    def clean_password(self):
        return self.initial['password']


class CustomUserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


@admin.register(User)
class FlisolUserAdmin(UserAdmin):
    u"""Administración de Usuarios
    """
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'is_staff',
        'is_superuser',
    )

    search_fields = ('first_name', 'last_name', 'email')

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            ),
        }),
        (u'Información personal', {
            'fields': (
                'first_name',
                'last_name',
            ),
        }),
        (u'Permisos', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
        (u'Fechas importantes', {
            'fields': (
                'last_login',
                'date_joined',
            ),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
    )

    ordering = ('first_name',)

    def get_actions(self, request):
        actions = super(FlisolUserAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        return (
            super(FlisolUserAdmin, self).get_readonly_fields(request, obj)
            + ('last_login', 'date_joined')
        )

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return False
