# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flisol_event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flisolinstance',
            name='address',
            field=models.CharField(default=b'', max_length=255, verbose_name='address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flisolinstance',
            name='flisol_event',
            field=models.ForeignKey(related_name='instances', verbose_name='event', to='flisol_event.FlisolEvent'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flisolinstance',
            name='schedule',
            field=models.CharField(default=b'', max_length=255, verbose_name='schedule', blank=True),
            preserve_default=True,
        ),
    ]
