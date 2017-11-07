# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('weddingServices', '0007_auto_20171106_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='catererbooking',
            name='cost',
            field=models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.0000')),
        ),
        migrations.AddField(
            model_name='floristbooking',
            name='cost',
            field=models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.0000')),
        ),
        migrations.AddField(
            model_name='hallbooking',
            name='cost',
            field=models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.0000')),
        ),
    ]
