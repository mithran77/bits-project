# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weddingServices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caterer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('shop_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=10)),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Florist',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('shop_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=10)),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('shop_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=10)),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='caterers',
            name='user',
        ),
        migrations.RemoveField(
            model_name='florists',
            name='user',
        ),
        migrations.RemoveField(
            model_name='halls',
            name='user',
        ),
        migrations.DeleteModel(
            name='Caterers',
        ),
        migrations.DeleteModel(
            name='Florists',
        ),
        migrations.DeleteModel(
            name='Halls',
        ),
    ]
