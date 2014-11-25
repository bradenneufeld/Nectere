# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20141125_0155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mfilteroptions',
            options={'ordering': ('matching_function',)},
        ),
    ]
