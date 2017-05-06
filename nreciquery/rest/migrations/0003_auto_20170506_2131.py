# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recipe',
            name='type',
            field=models.CharField(choices=[('ST', 'Started'), ('MD', 'Main Dish'), ('SD', 'Side Dish'), ('SN', 'Snack'), ('DS', 'Dessert')], default='MD', max_length=2),
        ),
    ]
