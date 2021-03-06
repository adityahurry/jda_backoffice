# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 02:04
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0007_auto_20170218_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standaloneevent',
            name='balloon_color',
            field=colorful.fields.RGBColorField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subevent',
            name='balloon_color',
            field=colorful.fields.RGBColorField(blank=True, null=True),
        ),
    ]
