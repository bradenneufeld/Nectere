# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20141124_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchfilterdata',
            old_name='value',
            new_name='primary_value',
        ),
        migrations.RenameField(
            model_name='matchpreferencedata',
            old_name='value',
            new_name='primary_value',
        ),
        migrations.RenameField(
            model_name='userfilterdata',
            old_name='value',
            new_name='primary_value',
        ),
        migrations.RenameField(
            model_name='userpreferencedata',
            old_name='value',
            new_name='primary_value',
        ),
    ]
