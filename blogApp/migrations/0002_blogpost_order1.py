# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-14 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='order1',
            field=models.IntegerField(default=0),
        ),
    ]
