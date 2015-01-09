# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20141217_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='iso_code',
            field=models.CharField(default=b'co', max_length=3, verbose_name='country code'),
            preserve_default=True,
        ),
    ]
