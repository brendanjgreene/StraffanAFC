# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170518_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.CharField(max_length=255, choices=[(b'U8', b'U8'), (b'U9', b'U9'), (b'U11 White', b'U11 White'), (b'U11 Green', b'U11 Green'), (b'U12', b'U12'), (b'U14', b'U14'), (b'Seniors', b'Seniors'), (b'Masters', b'Masters')]),
        ),
    ]
