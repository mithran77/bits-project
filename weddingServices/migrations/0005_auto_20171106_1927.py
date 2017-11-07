# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weddingServices', '0004_auto_20171106_1355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catererbooking',
            old_name='date',
            new_name='booking_date',
        ),
        migrations.RenameField(
            model_name='floristbooking',
            old_name='date',
            new_name='booking_date',
        ),
        migrations.RenameField(
            model_name='hallbooking',
            old_name='date',
            new_name='booking_date',
        ),
    ]
