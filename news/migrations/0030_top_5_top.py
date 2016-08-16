# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0029_auto_20160627_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='top_5',
            name='top',
            field=models.CharField(choices=[('Top - 1', 'Top - 1'), ('Top - 2', 'Top - 2'), ('Top - 3', 'Top - 3'), ('Top - 4', 'Top - 4'), ('Top - 5', 'Top - 5')], default='', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]