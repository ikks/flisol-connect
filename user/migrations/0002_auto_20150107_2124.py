# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha de alta'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(verbose_name='profile description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=75, verbose_name='email'),
            preserve_default=True,
        ),
    ]
