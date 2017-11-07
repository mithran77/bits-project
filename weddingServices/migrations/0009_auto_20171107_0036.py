# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('weddingServices', '0008_auto_20171106_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floristbooking',
            name='booking_date',
            field=models.DateField(max_length=50, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='floristbooking',
            name='time_slots',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200),
        ),
        migrations.AlterField(
            model_name='hallbooking',
            name='booking_date',
            field=models.DateField(max_length=50, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='hallbooking',
            name='time_slots',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200),
        ),
    ]
