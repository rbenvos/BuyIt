# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_device', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('type', models.CharField(blank=True, max_length=3, choices=[(b'SP', b'Smartphone'), (b'TB', b'Tablet')])),
                ('os', models.CharField(blank=True, max_length=3, choices=[(b'iOS', b'iOS'), (b'And', b'Android'), (b'Moz', b'MozillaOS'), (b'Win', b'Windows phone')])),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modified_at', models.DateTimeField(default=datetime.datetime.now, editable=False, blank=True)),
            ],
        ),
    ]
