# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_services_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='pid',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
