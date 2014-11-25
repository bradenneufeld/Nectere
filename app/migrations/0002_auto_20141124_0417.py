# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matchfilterdata',
            options={'ordering': ('filter',)},
        ),
        migrations.AlterModelOptions(
            name='matchpreferencedata',
            options={'ordering': ('filter',)},
        ),
        migrations.AlterModelOptions(
            name='userfilterdata',
            options={'ordering': ('filter',)},
        ),
        migrations.AlterModelOptions(
            name='userpreferencedata',
            options={'ordering': ('filter',)},
        ),
        migrations.AlterField(
            model_name='matchfilterdata',
            name='user',
            field=models.ForeignKey(to='app.User', related_name='match_filters'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='matchpreferencedata',
            name='user',
            field=models.ForeignKey(to='app.User', related_name='match_preferences'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userfilterdata',
            name='user',
            field=models.ForeignKey(to='app.User', related_name='user_filters'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userpreferencedata',
            name='user',
            field=models.ForeignKey(to='app.User', related_name='user_preferences'),
            preserve_default=True,
        ),
    ]
