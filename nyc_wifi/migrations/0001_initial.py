# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-29 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WifiSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borough', models.CharField(max_length=2)),
                ('type', models.CharField(max_length=50)),
                ('provider', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('location_type', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('ssid', models.CharField(max_length=50)),
            ],
        ),
    ]
