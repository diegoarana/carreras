# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-20 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcarreras', '0006_auto_20161020_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valoracion',
            name='calificacion',
            field=models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
    ]
