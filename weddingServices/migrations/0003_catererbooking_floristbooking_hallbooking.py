# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import multiselectfield.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weddingServices', '0002_auto_20171019_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatererBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time_slots', multiselectfield.db.fields.MultiSelectField(max_length=8, choices=[('FN', 'Forenoon [8-12]'), ('AN', 'Afternoon [2-5]'), ('EV', 'Evening [6-10]')])),
                ('caterer', models.ForeignKey(to='weddingServices.Caterer', related_name='hall')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='caterer_user')),
            ],
        ),
        migrations.CreateModel(
            name='FloristBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time_slots', multiselectfield.db.fields.MultiSelectField(max_length=8, choices=[('FN', 'Forenoon [8-12]'), ('AN', 'Afternoon [2-5]'), ('EV', 'Evening [6-10]')])),
                ('florist', models.ForeignKey(to='weddingServices.Florist', related_name='hall')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='florist_user')),
            ],
        ),
        migrations.CreateModel(
            name='HallBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time_slots', multiselectfield.db.fields.MultiSelectField(max_length=8, choices=[('FN', 'Forenoon [8-12]'), ('AN', 'Afternoon [2-5]'), ('EV', 'Evening [6-10]')])),
                ('hall', models.ForeignKey(to='weddingServices.Hall', related_name='hall')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='hall_user')),
            ],
        ),
    ]
