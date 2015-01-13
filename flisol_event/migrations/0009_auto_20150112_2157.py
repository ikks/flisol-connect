# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flisol_event', '0008_auto_20150112_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flisolinstance',
            name='wiki_url',
            field=models.URLField(verbose_name='wiki url'),
            preserve_default=True,
        ),
    ]
