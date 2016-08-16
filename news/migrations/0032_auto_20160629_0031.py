# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0031_auto_20160628_2346'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Top_5',
        ),
        migrations.AlterField(
            model_name='card',
            name='top',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Top - 1', 'Top - 1'), ('Top - 2', 'Top - 2'), ('Top - 3', 'Top - 3'), ('Top - 4', 'Top - 4'), ('Top - 5', 'Top - 5')], max_length=50),
        ),
    ]