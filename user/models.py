#! /usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import hashlib
import urllib2
import time

from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.core.files.base import ContentFile


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            is_active=is_active,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    first_name = models.CharField(
        verbose_name=u'nombres',
        max_length=128,
        blank=False,
        validators=[
            MinLengthValidator(3),
        ],
        error_messages={
            'min_length': (
                u'El campo "Nombres" debe tener al menos %(limit_value)d '
                u'caracteres (actualmente tiene %(show_value)d).'
            )
        }
    )

    last_name = models.CharField(
        verbose_name=u'apellidos',
        max_length=128,
        blank=False,
        validators=[
            MinLengthValidator(3),
        ],
        error_messages={
            'min_length': (
                u'El campo "Apellidos" debe tener al menos %(limit_value)d '
                u'caracteres (actualmente tiene %(show_value)d).'
            )
        }
    )

    email = models.EmailField(
        verbose_name=_('email'),
        unique=True,
        blank=False,
    )

    is_staff = models.BooleanField(
        u'staff status',
        default=False,
        help_text=u'Indica si el usuario puede entrar en este sitio '
                  u'de administración.',
    )

    is_active = models.BooleanField(
        u'Activo',
        default=True,
        help_text=u'Indica si el usuario puede ser tratado como activo. '
                  u'Desmarque esta opción en lugar de borrar la cuenta.',
    )
    date_joined = models.DateTimeField(
        verbose_name=_('date joined'),
        default=timezone.now,
    )

    avatar = models.ImageField(
        upload_to='user/avatar/',
        max_length=255,
        blank=True,
    )

    description = models.TextField(
        blank=True,
        verbose_name=_('profile description'),
    )

    objects = UserManager()

    def get_full_name(self):
        full_name = u'{0} {1}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        short_name = u'{0}'.format(self.first_name)
        return short_name.strip()

    def __unicode__(self):
        return u'{0}'.format(self.get_full_name())

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('email',)


@receiver(post_save, sender=User)
def put_gravatar(sender, created, instance, **kwargs):
    if not created:
        return

    email = instance.email
    default = "http://www.stevensegallery.com/40/40"
    size = 40

    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
    instance.avatar.save(
        u'{0}.jpg'.format(int(time.time())),
        ContentFile(urllib2.urlopen(gravatar_url).read()),
    )
