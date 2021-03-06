# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-05 14:52
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundo', '0006_linhaonibus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadastro', models.FloatField()),
                ('observacao', models.CharField(max_length=254)),
                ('geo_id', models.FloatField()),
                ('tipo', models.FloatField()),
                ('num_lote', models.CharField(max_length=254)),
                ('testada', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
