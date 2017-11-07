# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weddingServices', '0005_auto_20171106_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='caterer',
            name='email',
            field=models.EmailField(max_length=70, blank=True),
        ),
        migrations.AddField(
            model_name='florist',
            name='email',
            field=models.EmailField(max_length=70, blank=True),
        ),
        migrations.AddField(
            model_name='hall',
            name='email',
            field=models.EmailField(max_length=70, blank=True),
        ),
    ]
