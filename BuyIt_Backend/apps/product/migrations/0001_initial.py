# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('purchased', models.BooleanField(default=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified_at', models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('quantity', models.PositiveIntegerField(default=0, blank=True)),
                ('measure', models.CharField(blank=True, max_length=3, choices=[(b'kg', b'Kilogramos'), (b'l', b'Litros')])),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified_at', models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(to='product.Product'),
        ),
    ]
