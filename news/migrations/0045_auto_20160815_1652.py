# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 11:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0044_smallcard'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Basic_configuration',
            new_name='BasicConfiguration',
        ),
    ]