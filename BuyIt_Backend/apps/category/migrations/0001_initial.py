# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('subcategory', models.FloatField(verbose_name=b'Subcategory', blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified_at', models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified_at', models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)),
            ],
        ),
    ]
