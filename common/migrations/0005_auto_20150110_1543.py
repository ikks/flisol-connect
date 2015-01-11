# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_country_iso_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribution',
            name='url',
            field=models.URLField(max_length=255, verbose_name='wikipedia link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='distribution',
            name='logo',
            field=models.ImageField(upload_to=b'common/distro/', max_length=255, verbose_name='image', blank=True),
            preserve_default=True,
        ),
    ]
