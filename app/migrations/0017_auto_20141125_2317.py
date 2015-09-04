# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20141125_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mfilteroptions',
            name='type',
            field=models.CharField(choices=[('m', 'Min'), ('M', 'Max'), ('A', 'Complementary A of A-B'), ('B', 'Complementary B of B-A'), ('N', 'normal')], max_length=1, default='N'),
            preserve_default=True,
        ),
    ]
