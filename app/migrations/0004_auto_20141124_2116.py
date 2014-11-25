# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20141124_0605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filteroptions',
            old_name='value',
            new_name='primary_value',
        ),
        migrations.AddField(
            model_name='filteroptions',
            name='secondary_value',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
