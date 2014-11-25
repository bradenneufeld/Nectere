# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20141125_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermatchmeta',
            name='user',
            field=models.ForeignKey(to='app.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userselfmeta',
            name='user',
            field=models.ForeignKey(to='app.User'),
            preserve_default=True,
        ),
    ]
