# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='age',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
