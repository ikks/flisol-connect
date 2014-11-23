# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='created_by',
            field=models.ForeignKey(related_name='countries_created', verbose_name='created by', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='distribution',
            name='created_by',
            field=models.ForeignKey(related_name='distros_created', verbose_name='created by', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
