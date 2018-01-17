# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('weddingServices', '0009_auto_20171107_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='caterer',
            name='lat',
            field=models.DecimalField(max_digits=10, decimal_places=5, default=Decimal('0.0000')),
        ),
        migrations.AddField(
            model_name='caterer',
            name='lng',
            field=models.DecimalField(max_digits=10, decimal_places=5, default=Decimal('0.0000')),
        ),
    ]
