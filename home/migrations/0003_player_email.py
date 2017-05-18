# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='email',
            field=models.CharField(default=datetime.datetime(2017, 5, 18, 9, 49, 32, 812432, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
