# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20170622_1726'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='team',
            field=models.ForeignKey(related_name='subject_team', default=1, to='home.Team'),
            preserve_default=False,
        ),
    ]
