# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20141123_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='description',
            field=models.TextField(verbose_name='descripci\xf3n', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='country',
            name='logo_flag',
            field=models.ImageField(upload_to=b'common/flag/', max_length=255, verbose_name='flag icon', blank=True),
            preserve_default=True,
        ),
    ]
