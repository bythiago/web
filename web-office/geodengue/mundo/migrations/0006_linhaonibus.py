# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-05 14:39
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundo', '0005_ciclovia'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinhaOnibus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=254)),
                ('empresa', models.CharField(max_length=254)),
                ('sentido', models.CharField(max_length=254)),
                ('n_linha', models.CharField(max_length=254)),
                ('descricao_field', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
        ),
    ]
