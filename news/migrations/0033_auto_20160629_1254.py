# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0032_auto_20160629_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='text',
            field=models.TextField(),
        ),
    ]