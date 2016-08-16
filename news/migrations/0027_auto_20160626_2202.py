# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0026_auto_20160626_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breaking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_color', models.CharField(choices=[(' ', 'AliceBlue'), (' ', 'AntiqueWhite'), (' ', 'Aqua'), (' ', 'Aquamarine'), (' ', 'Azure'), (' ', 'Beige'), (' ', 'Bisque'), (' ', 'Black'), (' ', 'BlanchedAlmond'), (' ', 'Blue'), (' ', 'BlueViolet'), (' ', 'Brown'), (' ', 'BurlyWood'), (' ', 'CadetBlue'), (' ', 'Chartreuse'), (' ', 'Chocolate'), (' ', 'Coral'), (' ', 'CornflowerBlue'), (' ', 'Cornsilk'), (' ', 'Crimson'), (' ', 'Cyan'), (' ', 'DarkBlue'), (' ', 'DarkCyan'), (' ', 'DarkGoldenRod'), (' ', 'DarkGray'), (' ', 'DarkGrey'), (' ', 'DarkGreen'), (' ', 'DarkKhaki'), (' ', 'DarkMagenta'), (' ', 'DarkOliveGreen'), (' ', 'DarkOrange'), (' ', 'DarkOrchid'), (' ', 'DarkRed'), (' ', 'DarkSalmon'), (' ', 'DarkSeaGreen'), (' ', 'DarkSlateBlue'), (' ', 'DarkSlateGray'), (' ', 'DarkSlateGrey'), (' ', 'DarkTurquoise'), (' ', 'DarkViolet'), (' ', 'DeepPink'), (' ', 'DeepSkyBlue'), (' ', 'DimGray'), (' ', 'DimGrey'), (' ', 'DodgerBlue'), (' ', 'FireBrick'), (' ', 'FloralWhite'), (' ', 'ForestGreen'), (' ', 'Fuchsia'), (' ', 'Gainsboro'), (' ', 'GhostWhite'), (' ', 'Gold'), (' ', 'GoldenRod'), (' ', 'Gray'), (' ', 'Grey'), (' ', 'Green'), (' ', 'GreenYellow'), (' ', 'HoneyDew'), (' ', 'HotPink'), (' ', 'IndianRed'), (' ', 'Indigo '), (' ', 'Ivory'), (' ', 'Khaki'), (' ', 'Lavender'), (' ', 'LavenderBlush'), (' ', 'LawnGreen'), (' ', 'LemonChiffon'), (' ', 'LightBlue'), (' ', 'LightCoral'), (' ', 'LightCyan'), (' ', 'LightGoldenRodYellow'), (' ', 'LightGray'), (' ', 'LightGrey'), (' ', 'LightGreen'), (' ', 'LightPink'), (' ', 'LightSalmon'), (' ', 'LightSeaGreen'), (' ', 'LightSkyBlue'), (' ', 'LightSlateGray'), (' ', 'LightSlateGrey'), (' ', 'LightSteelBlue'), (' ', 'LightYellow'), (' ', 'Lime'), (' ', 'LimeGreen'), (' ', 'Linen'), (' ', 'Magenta'), (' ', 'Maroon'), (' ', 'MediumAquaMarine'), (' ', 'MediumBlue'), (' ', 'MediumOrchid'), (' ', 'MediumPurple'), (' ', 'MediumSeaGreen'), (' ', 'MediumSlateBlue'), (' ', 'MediumSpringGreen'), (' ', 'MediumTurquoise'), (' ', 'MediumVioletRed'), (' ', 'MidnightBlue'), (' ', 'MintCream'), (' ', 'MistyRose'), (' ', 'Moccasin'), (' ', 'NavajoWhite'), (' ', 'Navy'), (' ', 'OldLace'), (' ', 'Olive'), (' ', 'OliveDrab'), (' ', 'Orange'), (' ', 'OrangeRed'), (' ', 'Orchid'), (' ', 'PaleGoldenRod'), (' ', 'PaleGreen'), (' ', 'PaleTurquoise'), (' ', 'PaleVioletRed'), (' ', 'PapayaWhip'), (' ', 'PeachPuff'), (' ', 'Peru'), (' ', 'Pink'), (' ', 'Plum'), (' ', 'PowderBlue'), (' ', 'Purple'), (' ', 'RebeccaPurple'), (' ', 'Red'), (' ', 'RosyBrown'), (' ', 'RoyalBlue'), (' ', 'SaddleBrown'), (' ', 'Salmon'), (' ', 'SandyBrown'), (' ', 'SeaGreen'), (' ', 'SeaShell'), (' ', 'Sienna'), (' ', 'Silver'), (' ', 'SkyBlue'), (' ', 'SlateBlue'), (' ', 'SlateGray'), (' ', 'SlateGrey'), (' ', 'Snow'), (' ', 'SpringGreen'), (' ', 'SteelBlue'), (' ', 'Tan'), (' ', 'Teal'), (' ', 'Thistle'), (' ', 'Tomato'), (' ', 'Turquoise'), (' ', 'Violet'), (' ', 'Wheat'), (' ', 'White'), (' ', 'WhiteSmoke'), (' ', 'Yellow'), (' ', 'YellowGreen')], max_length=50)),
                ('font_color', models.CharField(choices=[(' ', 'White'), (' ', 'Black')], max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('text', tinymce.models.HTMLField()),
                ('intro_text', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='card/')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', tinymce.models.HTMLField()),
                ('image', models.ImageField(upload_to='slide/')),
            ],
        ),
        migrations.CreateModel(
            name='Top_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', tinymce.models.HTMLField()),
                ('background_color', models.CharField(choices=[(' ', 'AliceBlue'), (' ', 'AntiqueWhite'), (' ', 'Aqua'), (' ', 'Aquamarine'), (' ', 'Azure'), (' ', 'Beige'), (' ', 'Bisque'), (' ', 'Black'), (' ', 'BlanchedAlmond'), (' ', 'Blue'), (' ', 'BlueViolet'), (' ', 'Brown'), (' ', 'BurlyWood'), (' ', 'CadetBlue'), (' ', 'Chartreuse'), (' ', 'Chocolate'), (' ', 'Coral'), (' ', 'CornflowerBlue'), (' ', 'Cornsilk'), (' ', 'Crimson'), (' ', 'Cyan'), (' ', 'DarkBlue'), (' ', 'DarkCyan'), (' ', 'DarkGoldenRod'), (' ', 'DarkGray'), (' ', 'DarkGrey'), (' ', 'DarkGreen'), (' ', 'DarkKhaki'), (' ', 'DarkMagenta'), (' ', 'DarkOliveGreen'), (' ', 'DarkOrange'), (' ', 'DarkOrchid'), (' ', 'DarkRed'), (' ', 'DarkSalmon'), (' ', 'DarkSeaGreen'), (' ', 'DarkSlateBlue'), (' ', 'DarkSlateGray'), (' ', 'DarkSlateGrey'), (' ', 'DarkTurquoise'), (' ', 'DarkViolet'), (' ', 'DeepPink'), (' ', 'DeepSkyBlue'), (' ', 'DimGray'), (' ', 'DimGrey'), (' ', 'DodgerBlue'), (' ', 'FireBrick'), (' ', 'FloralWhite'), (' ', 'ForestGreen'), (' ', 'Fuchsia'), (' ', 'Gainsboro'), (' ', 'GhostWhite'), (' ', 'Gold'), (' ', 'GoldenRod'), (' ', 'Gray'), (' ', 'Grey'), (' ', 'Green'), (' ', 'GreenYellow'), (' ', 'HoneyDew'), (' ', 'HotPink'), (' ', 'IndianRed'), (' ', 'Indigo '), (' ', 'Ivory'), (' ', 'Khaki'), (' ', 'Lavender'), (' ', 'LavenderBlush'), (' ', 'LawnGreen'), (' ', 'LemonChiffon'), (' ', 'LightBlue'), (' ', 'LightCoral'), (' ', 'LightCyan'), (' ', 'LightGoldenRodYellow'), (' ', 'LightGray'), (' ', 'LightGrey'), (' ', 'LightGreen'), (' ', 'LightPink'), (' ', 'LightSalmon'), (' ', 'LightSeaGreen'), (' ', 'LightSkyBlue'), (' ', 'LightSlateGray'), (' ', 'LightSlateGrey'), (' ', 'LightSteelBlue'), (' ', 'LightYellow'), (' ', 'Lime'), (' ', 'LimeGreen'), (' ', 'Linen'), (' ', 'Magenta'), (' ', 'Maroon'), (' ', 'MediumAquaMarine'), (' ', 'MediumBlue'), (' ', 'MediumOrchid'), (' ', 'MediumPurple'), (' ', 'MediumSeaGreen'), (' ', 'MediumSlateBlue'), (' ', 'MediumSpringGreen'), (' ', 'MediumTurquoise'), (' ', 'MediumVioletRed'), (' ', 'MidnightBlue'), (' ', 'MintCream'), (' ', 'MistyRose'), (' ', 'Moccasin'), (' ', 'NavajoWhite'), (' ', 'Navy'), (' ', 'OldLace'), (' ', 'Olive'), (' ', 'OliveDrab'), (' ', 'Orange'), (' ', 'OrangeRed'), (' ', 'Orchid'), (' ', 'PaleGoldenRod'), (' ', 'PaleGreen'), (' ', 'PaleTurquoise'), (' ', 'PaleVioletRed'), (' ', 'PapayaWhip'), (' ', 'PeachPuff'), (' ', 'Peru'), (' ', 'Pink'), (' ', 'Plum'), (' ', 'PowderBlue'), (' ', 'Purple'), (' ', 'RebeccaPurple'), (' ', 'Red'), (' ', 'RosyBrown'), (' ', 'RoyalBlue'), (' ', 'SaddleBrown'), (' ', 'Salmon'), (' ', 'SandyBrown'), (' ', 'SeaGreen'), (' ', 'SeaShell'), (' ', 'Sienna'), (' ', 'Silver'), (' ', 'SkyBlue'), (' ', 'SlateBlue'), (' ', 'SlateGray'), (' ', 'SlateGrey'), (' ', 'Snow'), (' ', 'SpringGreen'), (' ', 'SteelBlue'), (' ', 'Tan'), (' ', 'Teal'), (' ', 'Thistle'), (' ', 'Tomato'), (' ', 'Turquoise'), (' ', 'Violet'), (' ', 'Wheat'), (' ', 'White'), (' ', 'WhiteSmoke'), (' ', 'Yellow'), (' ', 'YellowGreen')], max_length=50)),
                ('font_color', models.CharField(choices=[(' ', 'White'), (' ', 'Black')], max_length=50)),
                ('intro_text', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='top/')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='Section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Section'),
        ),
    ]
