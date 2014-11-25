# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20141125_0432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_meta',
            new_name='self_meta',
        ),
        migrations.AlterField(
            model_name='userselfmeta',
            name='option',
            field=models.ForeignKey(related_name='self_meta', to='app.MFilterOptions'),
            preserve_default=True,
        ),
    ]
