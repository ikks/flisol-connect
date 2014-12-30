#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _


class FlisolEvent(models.Model):
    """Each year a flisol event takes place, this model
    allows to have different events per year
    """

    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
    )

    slug = models.SlugField(
        unique=True,
    )

    logo = models.ImageField(
        max_length=255,
        upload_to='flisol/event/',
        verbose_name=_('image'),
    )

    description = models.TextField(
        verbose_name=_('description'),
    )

    official_date = models.DateField(
        verbose_name=_('official date'),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at'),
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('created by'),
        related_name='events_created',
    )

    def __unicode__(self):
        return u'{0}'.format(self.name)

    class Meta:
        verbose_name = _('flisol event')
        verbose_name_plural = _('flisol events')
        ordering = ('name',)


class FlisolInstanceRequest(models.Model):

    city_name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
    )

    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at'),
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('created by'),
        related_name='cities_requested',
    )

    flisol_event = models.ForeignKey(
        'flisol_event.FlisolEvent',
        verbose_name=_('created by'),
        related_name='cities_to_create',
    )

    def __unicode__(self):
        return u'{0}'.format(self.name)

    class Meta:
        verbose_name = _('flisol city request')
        verbose_name_plural = _('flisol city requests')
        ordering = ('city_name',)


class FlisolInstance(models.Model):
    INSTANCE_STATUS_CREATED = 10
    INSTANCE_STATUS_PLANNING = 20
    INSTANCE_STATUS_WILL_DO = 30
    INSTANCE_STATUS_READY = 40
    INSTANCE_STATUS_FULL = 50
    INSTANCE_STATUS_IN_PROGRESS = 60
    INSTANCE_STATUS_DONE = 70
    INSTANCE_STATUS_CHOICES = (
        (INSTANCE_STATUS_CREATED, _('created')),
        (INSTANCE_STATUS_PLANNING, _('planning')),
        (INSTANCE_STATUS_WILL_DO, _('will do')),
        (INSTANCE_STATUS_READY, _('ready')),
        (INSTANCE_STATUS_FULL, _('full')),
        (INSTANCE_STATUS_IN_PROGRESS, _('happening')),
        (INSTANCE_STATUS_DONE, _('done')),
    )

    city_name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
    )

    instance_name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
    )

    slug = models.SlugField(
        unique=True,
    )

    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
    )

    address = models.CharField(
        max_length=255,
        verbose_name=_('address'),
        default='',
        blank=True,
    )

    schedule = models.CharField(
        max_length=255,
        verbose_name=_('schedule'),
        default='',
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

    image = models.ImageField(
        max_length=255,
        upload_to='flisol/instance/',
        verbose_name=_('country banner image'),
        blank=True,
    )

    status = models.PositiveSmallIntegerField(
        default=10,
        choices=INSTANCE_STATUS_CHOICES,
        verbose_name=_('status'),
    )

    email_contact = models.EmailField(
        verbose_name=_('email contact'),
        help_text=_('please ask for a mail list'),
        unique=True,
        blank=False,
    )

    wiki_url = models.URLField(
        verbose_name=u'wiki url',
        unique=True,
        blank=False,
    )

    instance_date = models.DateField(
        auto_now_add=True,
        verbose_name=_('date'),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at'),
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('created by'),
        related_name='instances_created',
    )

    flisol_event = models.ForeignKey(
        'flisol_event.FlisolEvent',
        verbose_name=_('event'),
        related_name='instances',
    )

    country = models.ForeignKey(
        'common.Country',
        verbose_name=_('country'),
        related_name='instances_of_country',
    )

    people = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='FlisolAttendance'
    )

    def __unicode__(self):
        return u'{0} {1}'.format(
            self.city_name,
            self.instance_name,
        )

    class Meta:
        verbose_name = _('flisol instance')
        verbose_name_plural = _('flisol instances')
        ordering = ('city_name', 'instance_name')


class FlisolAttendance(models.Model):
    ATTENDANCE_CHOICES_VISITOR = 10
    ATTENDANCE_CHOICES_VOLUNTEER = 20
    ATTENDANCE_CHOICES_INSTALLER = 30
    ATTENDANCE_CHOICES_OTHER = 100
    ATTENDANCE_CHOICES_CHOICES = (
        (ATTENDANCE_CHOICES_VISITOR, _('visitor')),
        (ATTENDANCE_CHOICES_VOLUNTEER, _('volunteer')),
        (ATTENDANCE_CHOICES_INSTALLER, _('installer')),
        (ATTENDANCE_CHOICES_OTHER, _('other')),
    )

    role = models.PositiveSmallIntegerField(
        default=10,
        choices=ATTENDANCE_CHOICES_CHOICES,
        verbose_name=_('role'),
    )

    flisol_instance = models.ForeignKey(
        'flisol_event.FlisolInstance',
        verbose_name=_('country'),
        related_name='attendants',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name='attendances',
    )

    can_update = models.BooleanField(
        verbose_name=('can update instance info'),
        default=False,
    )

    def __unicode__(self):
        return u'{0}'.format(self.user.get_full_name())

    class Meta:
        verbose_name = _('instance flisol person')
        verbose_name_plural = _('instance flisol people')
        ordering = ('-id',)


class FlisolMachine(models.Model):
    MACHINE_TYPE_CHOICES_DESKTOP = 10
    MACHINE_TYPE_CHOICES_LAPTOP = 20
    MACHINE_TYPE_CHOICES_TABLET = 30
    MACHINE_TYPE_CHOICES_CELL_PHONE = 40
    MACHINE_TYPE_CHOICES_CHOICES = (
        (MACHINE_TYPE_CHOICES_DESKTOP, _('desktop')),
        (MACHINE_TYPE_CHOICES_LAPTOP, _('laptop')),
        (MACHINE_TYPE_CHOICES_TABLET, _('tablet')),
        (MACHINE_TYPE_CHOICES_CELL_PHONE, _('phone')),
    )

    is_installed = models.BooleanField(
        verbose_name=('is installed'),
        default=False,
    )

    machine_type = models.PositiveSmallIntegerField(
        default=10,
        choices=MACHINE_TYPE_CHOICES_CHOICES,
        verbose_name=_('machine_type'),
    )

    registar = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('registar'),
        related_name='machines_registered',
    )

    installed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('installed_by'),
        related_name='machines_installed',
        null=True,
    )

    requested_distro = models.ForeignKey(
        'common.Distribution',
        verbose_name=_('requested distro'),
        related_name='machines_requesting',
        null=True,
    )

    installed_distro = models.ForeignKey(
        'common.Distribution',
        verbose_name=_('installed distro'),
        related_name='machines',
        null=True,
    )

    description = models.TextField(
        verbose_name=_('description'),
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at'),
    )

    installed_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('installed at'),
    )
