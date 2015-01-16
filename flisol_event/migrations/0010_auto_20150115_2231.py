# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flisol_event', '0009_auto_20150112_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flisolmachine',
            name='installed_distro',
            field=models.ForeignKey(related_name='machines', verbose_name='installed distro', blank=True, to='common.Distribution', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='flisolmachine',
            name='requested_distro',
            field=models.ForeignKey(related_name='machines_requesting', verbose_name='requested distro', blank=True, to='common.Distribution', null=True),
            preserve_default=True,
        ),
    ]
