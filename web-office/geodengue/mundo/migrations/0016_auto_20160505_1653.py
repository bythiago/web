# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-05 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundo', '0015_auto_20160505_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tra_trecho_rodoviario_l',
            name='administra',
            field=models.CharField(max_length=28),
        ),
        migrations.AlterField(
            model_name='tra_trecho_rodoviario_l',
            name='canteirodi',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tra_trecho_rodoviario_l',
            name='codtrechor',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='tra_trecho_rodoviario_l',
            name='concession',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='tra_trecho_rodoviario_l',
            name='jurisdicao',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tra_trecho_rodoviario_l',
            name='operaciona',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='tra_trecho_rodoviario_l',
            name='revestimen',
            field=models.CharField(max_length=39),
        ),
        migrations.AlterField(
            model_name='tra_trecho_rodoviario_l',
            name='situacaofi',
            field=models.CharField(max_length=23),
        ),
        migrations.AlterField(
            model_name='tra_trecho_rodoviario_l',
            name='tipotrecho',
            field=models.CharField(max_length=28),
        ),
        migrations.AlterField(
            model_name='tra_trecho_rodoviario_l',
            name='trafego',
            field=models.CharField(max_length=22),
        ),
    ]
