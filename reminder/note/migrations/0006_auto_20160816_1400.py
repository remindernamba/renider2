# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 08:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20160816_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='date_of_publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 8, 16, 8, 0, 0, 28493, tzinfo=utc), null=True, verbose_name='\u0414\u0430\u0442\u0430 \u041f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438'),
        ),
    ]
