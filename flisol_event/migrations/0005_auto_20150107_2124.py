# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flisol_event', '0004_auto_20141229_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='flisolattendance',
            name='comment',
            field=models.TextField(help_text='let us know how you can help best', verbose_name='comment', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flisolmachine',
            name='comment',
            field=models.TextField(verbose_name='comment post installation', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flisolmachine',
            name='flisol_instance',
            field=models.ForeignKey(related_name='machines', default=1, verbose_name='instance', to='flisol_event.FlisolInstance'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flisolattendance',
            name='flisol_instance',
            field=models.ForeignKey(related_name='attendants', verbose_name='instance', to='flisol_event.FlisolInstance'),
            preserve_default=True,
        ),
    ]
