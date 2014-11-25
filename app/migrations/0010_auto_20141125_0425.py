# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20141125_0205'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMatchMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user_value', models.IntegerField()),
                ('option', models.ForeignKey(to='app.MFilterOptions', related_name='match_meta')),
                ('user', models.ForeignKey(to='app.User', related_name='meta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserSelfMeta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('user_value', models.IntegerField()),
                ('option', models.ForeignKey(to='app.MFilterOptions', related_name='user_meta')),
                ('user', models.ForeignKey(to='app.User', related_name='self')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='usermfilter',
            name='m_filter',
        ),
        migrations.RemoveField(
            model_name='usermfilter',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserMFilter',
        ),
        migrations.RenameField(
            model_name='mfilteroptions',
            old_name='match_id',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='mfilteroptions',
            old_name='user_value',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='mfilteroptions',
            name='match_value',
        ),
        migrations.RemoveField(
            model_name='user',
            name='m_filter_options',
        ),
        migrations.AddField(
            model_name='user',
            name='match_meta',
            field=models.ManyToManyField(through='app.UserMatchMeta', related_name='meta', to='app.MFilterOptions'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='user_meta',
            field=models.ManyToManyField(through='app.UserSelfMeta', related_name='self', to='app.MFilterOptions'),
            preserve_default=True,
        ),
    ]
