# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flisol_event', '0005_auto_20150107_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='flisolinstancerequest',
            name='country',
            field=models.CharField(default=b'co', max_length=3, verbose_name='country code'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flisolinstancerequest',
            name='map_center',
            field=models.CharField(default=b'-85.627,13.176', help_text='lat,lon', max_length=255, verbose_name='map center on'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flisolinstance',
            name='city_name',
            field=models.CharField(max_length=255, verbose_name='city'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flisolinstance',
            name='instance_name',
            field=models.CharField(max_length=255, verbose_name='instance'),
            preserve_default=True,
        ),
    ]
