# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_subject_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='team',
        ),
    ]
