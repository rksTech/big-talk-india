# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20160608_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to='slide/'),
        ),
    ]
