# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20170518_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='team_name',
            new_name='name',
        ),
    ]
