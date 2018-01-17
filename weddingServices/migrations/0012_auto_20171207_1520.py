# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weddingServices', '0011_auto_20171207_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caterer',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
