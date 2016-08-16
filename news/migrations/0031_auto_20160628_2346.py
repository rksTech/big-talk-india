# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0030_top_5_top'),
    ]

    operations = [
        migrations.AddField(
            model_name='breaking',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='top',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Top - 1', 'Top - 1'), ('Top - 2', 'Top - 2'), ('Top - 3', 'Top - 3'), ('Top - 4', 'Top - 4'), ('Top - 5', 'Top - 5')], default='', max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slide',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Deactive', 'Deactive')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='top_5',
            name='top',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Top - 1', 'Top - 1'), ('Top - 2', 'Top - 2'), ('Top - 3', 'Top - 3'), ('Top - 4', 'Top - 4'), ('Top - 5', 'Top - 5')], max_length=50, unique=True),
        ),
    ]
