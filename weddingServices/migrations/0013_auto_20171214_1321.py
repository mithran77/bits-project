# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('weddingServices', '0012_auto_20171207_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='florist',
            name='lat',
            field=models.DecimalField(default=Decimal('0.0000'), max_digits=10, decimal_places=8),
        ),
        migrations.AddField(
            model_name='florist',
            name='lng',
            field=models.DecimalField(default=Decimal('0.0000'), max_digits=10, decimal_places=8),
        ),
        migrations.AddField(
            model_name='hall',
            name='lat',
            field=models.DecimalField(default=Decimal('0.0000'), max_digits=10, decimal_places=8),
        ),
        migrations.AddField(
            model_name='hall',
            name='lng',
            field=models.DecimalField(default=Decimal('0.0000'), max_digits=10, decimal_places=8),
        ),
        migrations.AlterField(
            model_name='florist',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='hall',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
