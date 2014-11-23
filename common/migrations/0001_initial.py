# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(verbose_name='descripci\xf3n')),
                ('logo_flag', models.ImageField(upload_to=b'common/flag/', max_length=255, verbose_name='flag icon')),
                ('image', models.ImageField(upload_to=b'common/country_banner/', max_length=255, verbose_name='country banner image', blank=True)),
                ('map_center', models.CharField(default=b'-85.627,13.176', help_text='lat,lon', max_length=255, verbose_name='map center on')),
                ('map_zoom', models.PositiveSmallIntegerField(default=6, verbose_name='default map zoom')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('slug', models.SlugField(unique=True)),
                ('logo', models.ImageField(upload_to=b'common/distro/', max_length=255, verbose_name='image')),
                ('description', models.TextField(verbose_name='descripci\xf3n')),
                ('wikipedia', models.URLField(max_length=255, verbose_name='wikipedia link', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('created_by', models.ForeignKey(verbose_name='created by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'distribution',
                'verbose_name_plural': 'distributions',
            },
            bases=(models.Model,),
        ),
    ]
