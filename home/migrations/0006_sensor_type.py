# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-03 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20171005_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='type',
            field=models.CharField(choices=[('P', 'Pluvial'), ('WS', 'Velocidad Viento'), ('UV', 'Luz Ultra Violeta)'), ('CO2', 'CO2')], default='Pluvial', max_length=255),
        ),
    ]