# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0003_auto_20170217_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardevent',
            name='address',
            field=models.CharField(max_length=255),
        ),
    ]