# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20160605_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slides',
            name='image_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]