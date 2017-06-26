# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_subject_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='team',
            field=models.ForeignKey(related_name='subject_team', blank=True, to='home.Team', null=True),
        ),
    ]
