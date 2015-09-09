# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified_at', models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified_at', models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='measure',
            field=models.ForeignKey(blank=True, to='product.Measure', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.ForeignKey(blank=True, to='product.Quantity', null=True),
        ),
    ]
