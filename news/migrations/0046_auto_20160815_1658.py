# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-15 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0045_auto_20160815_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='smallcard',
            name='image',
            field=models.ImageField(upload_to='small card/'),
        ),
    ]