# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-07 05:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_blogpost_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='feedback',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='short_description',
            field=models.TextField(default=datetime.datetime(2016, 5, 7, 5, 32, 7, 868000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
