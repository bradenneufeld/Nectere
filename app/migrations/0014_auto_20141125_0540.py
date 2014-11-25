# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20141125_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermatchmeta',
            name='option',
            field=models.ForeignKey(related_name='meta_option', to='app.MFilterOptions'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usermatchmeta',
            name='user',
            field=models.ForeignKey(related_name='meta', to='app.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userselfmeta',
            name='option',
            field=models.ForeignKey(related_name='self_option', to='app.MFilterOptions'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userselfmeta',
            name='user',
            field=models.ForeignKey(related_name='self', to='app.User'),
            preserve_default=True,
        ),
    ]
