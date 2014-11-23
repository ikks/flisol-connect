# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20141123_1242'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlisolAttendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.PositiveSmallIntegerField(default=10, verbose_name='role', choices=[(10, 'visitor'), (20, 'volunteer'), (30, 'installer'), (100, 'other')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('can_update', models.BooleanField(default=False, verbose_name=b'can update instance info')),
            ],
            options={
                'ordering': ('-id',),
                'verbose_name': 'instance flisol person',
                'verbose_name_plural': 'instance flisol people',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlisolEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('slug', models.SlugField(unique=True)),
                ('logo', models.ImageField(upload_to=b'flisol/event/', max_length=255, verbose_name='image')),
                ('description', models.TextField(verbose_name='descripci\xf3n')),
                ('official_date', models.DateField(auto_now_add=True, verbose_name='official date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('created_by', models.ForeignKey(related_name='events_created', verbose_name='created by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'flisol event',
                'verbose_name_plural': 'flisol events',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlisolInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city_name', models.CharField(max_length=255, verbose_name='nombre')),
                ('instance_name', models.CharField(max_length=255, verbose_name='nombre')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(verbose_name='descripci\xf3n', blank=True)),
                ('address', models.CharField(max_length=255, verbose_name='address')),
                ('schedule', models.CharField(max_length=255, verbose_name='schedule')),
                ('map_center', models.CharField(default=b'-85.627,13.176', help_text='lat,lon', max_length=255, verbose_name='map center on')),
                ('map_zoom', models.PositiveSmallIntegerField(default=6, verbose_name='default map zoom')),
                ('image', models.ImageField(upload_to=b'flisol/instance/', max_length=255, verbose_name='country banner image', blank=True)),
                ('status', models.PositiveSmallIntegerField(default=10, verbose_name='estado', choices=[(10, 'creado'), (20, 'planning'), (30, 'will do'), (40, 'ready'), (50, 'full'), (60, 'happening'), (70, 'done')])),
                ('email_contact', models.EmailField(help_text='please ask for a mail list', unique=True, max_length=75, verbose_name='email contact')),
                ('wiki_url', models.URLField(unique=True, verbose_name='wiki url')),
                ('instance_date', models.DateField(auto_now_add=True, verbose_name='date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('country', models.ForeignKey(related_name='instances_of_country', verbose_name='country', to='common.Country')),
                ('created_by', models.ForeignKey(related_name='instances_created', verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('flisol_event', models.ForeignKey(related_name='instances', verbose_name='created by', to='flisol_event.FlisolEvent')),
                ('people', models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='flisol_event.FlisolAttendance')),
            ],
            options={
                'ordering': ('city_name', 'instance_name'),
                'verbose_name': 'flisol city request',
                'verbose_name_plural': 'flisol city requests',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlisolInstanceRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city_name', models.CharField(max_length=255, verbose_name='nombre')),
                ('description', models.TextField(verbose_name='descripci\xf3n', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('created_by', models.ForeignKey(related_name='cities_requested', verbose_name='created by', to=settings.AUTH_USER_MODEL)),
                ('flisol_event', models.ForeignKey(related_name='cities_to_create', verbose_name='created by', to='flisol_event.FlisolEvent')),
            ],
            options={
                'ordering': ('city_name',),
                'verbose_name': 'flisol city request',
                'verbose_name_plural': 'flisol city requests',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlisolMachine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_installed', models.BooleanField(default=False, verbose_name=b'is installed')),
                ('machine_type', models.PositiveSmallIntegerField(default=10, verbose_name='machine_type', choices=[(10, 'desktop'), (20, 'laptop'), (30, 'tablet'), (40, 'phone')])),
                ('description', models.TextField(verbose_name='descripci\xf3n', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('installed_at', models.DateTimeField(auto_now_add=True, verbose_name='installed at')),
                ('installed_by', models.ForeignKey(related_name='machines_installed', verbose_name='installed_by', to=settings.AUTH_USER_MODEL, null=True)),
                ('installed_distro', models.ForeignKey(related_name='machines', verbose_name='installed distro', to='common.Distribution', null=True)),
                ('registar', models.ForeignKey(related_name='machines_registered', verbose_name='registar', to=settings.AUTH_USER_MODEL)),
                ('requested_distro', models.ForeignKey(related_name='machines_requesting', verbose_name='requested distro', to='common.Distribution', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='flisolattendance',
            name='flisol_instance',
            field=models.ForeignKey(related_name='instances_of_country', verbose_name='country', to='flisol_event.FlisolInstance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flisolattendance',
            name='user',
            field=models.ForeignKey(related_name='cities_to_create', verbose_name='usuario', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
