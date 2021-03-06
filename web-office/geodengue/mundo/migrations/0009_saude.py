# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-05 14:56
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundo', '0008_delete_lote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidade', models.IntegerField()),
                ('descricao', models.CharField(max_length=254)),
                ('endereco', models.CharField(max_length=254)),
                ('tel_ramal', models.CharField(max_length=254)),
                ('tipo', models.CharField(max_length=254)),
                ('hora_funci', models.CharField(max_length=254)),
                ('responsave', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
    ]
