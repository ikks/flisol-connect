# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flisol_event', '0002_auto_20141227_1935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flisolinstance',
            options={'ordering': ('city_name', 'instance_name'), 'verbose_name': 'flisol instance', 'verbose_name_plural': 'flisol instances'},
        ),
        migrations.AlterField(
            model_name='flisolevent',
            name='official_date',
            field=models.DateField(verbose_name='official date'),
            preserve_default=True,
        ),
    ]
