# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('weddingServices', '0010_auto_20171207_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caterer',
            name='lat',
            field=models.DecimalField(max_digits=10, default=Decimal('0.0000'), decimal_places=8),
        ),
        migrations.AlterField(
            model_name='caterer',
            name='lng',
            field=models.DecimalField(max_digits=10, default=Decimal('0.0000'), decimal_places=8),
        ),
    ]
