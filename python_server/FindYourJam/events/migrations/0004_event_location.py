# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170129_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='Toronto', max_length=50),
        ),
    ]
