# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20141125_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermatchmeta',
            name='m_filter',
            field=models.ForeignKey(related_name='user_match_meta', default=0, to='app.MFilter'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userselfmeta',
            name='m_filter',
            field=models.ForeignKey(related_name='user_self_meta', default=0, to='app.MFilter'),
            preserve_default=False,
        ),
    ]
