# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_remove_card_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='heading',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.Heading'),
            preserve_default=False,
        ),
    ]
