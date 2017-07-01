# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_team_age'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['age']},
        ),
    ]
