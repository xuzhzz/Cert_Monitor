# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20171115_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certinfo',
            name='end_date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='certinfo',
            name='start_date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='monitorinfo',
            name='current_date',
            field=models.CharField(max_length=30),
        ),
    ]
