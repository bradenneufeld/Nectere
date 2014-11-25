# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141124_0417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filteroptions',
            old_name='match_function',
            new_name='filter',
        ),
    ]
