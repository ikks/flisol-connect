# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=128, error_messages={b'min_length': 'El campo "Nombres" debe tener al menos %(limit_value)d caracteres (actualmente tiene %(show_value)d).'}, verbose_name='nombres', validators=[django.core.validators.MinLengthValidator(3)])),
                ('last_name', models.CharField(max_length=128, error_messages={b'min_length': 'El campo "Apellidos" debe tener al menos %(limit_value)d caracteres (actualmente tiene %(show_value)d).'}, verbose_name='apellidos', validators=[django.core.validators.MinLengthValidator(3)])),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name='correo electr\xf3nico')),
                ('is_staff', models.BooleanField(default=False, help_text='Indica si el usuario puede entrar en este sitio de administraci\xf3n.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Indica si el usuario puede ser tratado como activo. Desmarque esta opci\xf3n en lugar de borrar la cuenta.', verbose_name='Activo')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de alta')),
                ('avatar', models.ImageField(max_length=255, upload_to=b'user/avatar/', blank=True)),
                ('description', models.TextField(verbose_name='descripci\xf3n del perfil', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('email',),
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
            bases=(models.Model,),
        ),
    ]
