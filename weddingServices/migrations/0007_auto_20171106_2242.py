# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('weddingServices', '0006_auto_20171106_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='caterer',
            name='session_cost',
            field=models.DecimalField(default=Decimal('0.0000'), decimal_places=2, max_digits=6),
        ),
        migrations.AddField(
            model_name='florist',
            name='session_cost',
            field=models.DecimalField(default=Decimal('0.0000'), decimal_places=2, max_digits=6),
        ),
        migrations.AddField(
            model_name='hall',
            name='session_cost',
            field=models.DecimalField(default=Decimal('0.0000'), decimal_places=2, max_digits=6),
        ),
    ]
