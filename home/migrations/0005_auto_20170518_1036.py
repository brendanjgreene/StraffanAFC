# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170518_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.CharField(max_length=255, choices=[(b'1', b'U8'), (b'2', b'U9'), (b'3', b'U11 White'), (b'4', b'U11 Green'), (b'5', b'U12'), (b'6', b'U14'), (b'7', b'Seniors'), (b'8', b'Masters')]),
        ),
    ]
