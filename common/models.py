#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _

class Country(models.Model):
    """Country Model"""

    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
    )

    slug = models.SlugField(
        unique=True,
    )

    description = models.TextField(
        verbose_name=_('description'),
    )

    logo_flag = models.ImageField(
        max_length=255,
        upload_to='common/flag/',
        verbose_name=_('flag icon'),
    )

    image = models.ImageField(
        max_length=255,
        upload_to='common/country_banner/',
        verbose_name=_('country banner image'),
        blank=True,
    )

    map_center = models.CharField(
        max_length=255,
        default='-85.627,13.176',
        help_text=_('lat,lon'),
        verbose_name=_('map center on'),
    )

    map_zoom = models.PositiveSmallIntegerField(
        default=6,
        verbose_name=_('default map zoom'),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at'),
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('created by'),
    )

    def __unicode__(self):
        return u'{0}'.format(self.name)

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')
        ordering = ('name',)


class Distribution(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
    )

    slug = models.SlugField(
        unique=True,
    )

    logo = models.ImageField(
        max_length=255,
        upload_to='common/distro/',
        verbose_name=_('image'),
    )

    description = models.TextField(
        verbose_name=_('description'),
    )

    wikipedia = models.URLField(
        max_length=255,
        verbose_name=_('wikipedia link'),
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at'),
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('created by'),
    )

    def __unicode__(self):
        return u'{0}'.format(self.name)

    class Meta:
        verbose_name = _('distribution')
        verbose_name_plural = _('distributions')
        ordering = ('name',)
