# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flisol_event', '0007_auto_20150110_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flisolevent',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flisolinstance',
            name='email_contact',
            field=models.EmailField(help_text='please ask for a mail list', max_length=75, verbose_name='email contact'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flisolinstance',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False),
            preserve_default=True,
        ),
    ]
