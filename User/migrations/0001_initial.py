# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-01 18:12
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='banner image')),
                ('url', models.URLField(verbose_name='url')),
                ('index', models.IntegerField(default=100, verbose_name='sequence')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
            ],
            options={
                'verbose_name': 'banner image',
                'verbose_name_plural': 'banner image',
            },
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creditnum', models.CharField(max_length=16, verbose_name='card number')),
                ('realname', models.CharField(max_length=30, verbose_name="card holder's name")),
                ('securitycode', models.CharField(max_length=3, verbose_name='securitycode')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
            ],
            options={
                'verbose_name': 'credit card',
                'verbose_name_plural': 'credit card',
            },
        ),
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='verified code')),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
                ('send_type', models.CharField(choices=[('register', 'register'), ('forget', 'find back password')], max_length=10)),
                ('send_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'email verify code',
                'verbose_name_plural': 'email verify code',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('logname', models.CharField(max_length=30, verbose_name="user's log in name")),
                ('hometown', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('interest', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y/%m')),
                ('follownum', models.IntegerField(default=0, verbose_name='follow number')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': "user's information",
                'verbose_name_plural': "user's information",
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='creditcard',
            name='logname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="user's logname"),
        ),
    ]
