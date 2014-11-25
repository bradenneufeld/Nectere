# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20141125_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mfilteroptions',
            name='users',
        ),
        migrations.AddField(
            model_name='user',
            name='m_filter_options',
            field=models.ManyToManyField(to='app.MFilterOptions'),
            preserve_default=True,
        ),
    ]
