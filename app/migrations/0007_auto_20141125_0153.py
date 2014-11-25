# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20141125_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='mfilteroptions',
            name='match_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfilteroptions',
            name='users',
            field=models.ManyToManyField(to='app.User'),
            preserve_default=True,
        ),
    ]
