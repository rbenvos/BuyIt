# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(unique=True, max_length=9)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrivateUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=200)),
                ('password', models.CharField(max_length=200, blank=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('last_name', models.CharField(max_length=200, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified_at', models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)),
                ('device', models.ManyToManyField(to='device.Device', blank=True)),
                ('friends', models.ManyToManyField(to='private_user.Friend', blank=True)),
                ('phones', models.ForeignKey(blank=True, to='private_user.Phone', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(to='private_user.PrivateUser', null=True),
        ),
    ]
