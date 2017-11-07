# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('weddingServices', '0003_catererbooking_floristbooking_hallbooking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catererbooking',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, max_length=50),
        ),
        migrations.AlterField(
            model_name='catererbooking',
            name='time_slots',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200),
        ),
    ]
