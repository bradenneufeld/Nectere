# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20141125_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mfilteroptions',
            name='type',
            field=models.CharField(max_length=1, choices=[('m', 'Min'), ('M', 'Max'), ('N', 'normal')], default='N'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usermatchmeta',
            name='user',
            field=models.ForeignKey(to='app.User', related_name='meta'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userselfmeta',
            name='user',
            field=models.ForeignKey(to='app.User', related_name='self'),
            preserve_default=True,
        ),
    ]
