# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20150110_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='url',
            field=models.URLField(max_length=255, verbose_name='official url', blank=True),
            preserve_default=True,
        ),
    ]
