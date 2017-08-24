# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170824_1240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['date_of_birth']},
        ),
    ]
