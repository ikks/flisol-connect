# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('flisol_event', '0003_auto_20141228_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flisolattendance',
            name='flisol_instance',
            field=models.ForeignKey(related_name='attendants', verbose_name='country', to='flisol_event.FlisolInstance'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flisolattendance',
            name='user',
            field=models.ForeignKey(related_name='attendances', verbose_name='usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
