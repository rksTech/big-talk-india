# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0041_basic_configuration_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmallSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
