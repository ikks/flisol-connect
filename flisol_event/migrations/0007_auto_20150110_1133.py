# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flisol_event', '0006_auto_20150108_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flisolmachine',
            name='comment',
            field=models.TextField(help_text='do you have a special thing to say about your machine or you?', verbose_name='comment post installation', blank=True),
            preserve_default=True,
        ),
    ]
