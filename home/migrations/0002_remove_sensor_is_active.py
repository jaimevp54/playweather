# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-03 21:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='is_active',
        ),
    ]
