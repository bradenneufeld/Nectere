# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20141124_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='MFilterOptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('user_value', models.IntegerField()),
                ('match_value', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserMFilter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('user_value', models.IntegerField()),
            ],
            options={
                'ordering': ('m_filter',),
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Filter',
            new_name='MFilter',
        ),
        migrations.RemoveField(
            model_name='filteroptions',
            name='filter',
        ),
        migrations.DeleteModel(
            name='FilterOptions',
        ),
        migrations.RemoveField(
            model_name='matchfilterdata',
            name='filter',
        ),
        migrations.RemoveField(
            model_name='matchfilterdata',
            name='user',
        ),
        migrations.DeleteModel(
            name='MatchFilterData',
        ),
        migrations.RemoveField(
            model_name='matchpreferencedata',
            name='filter',
        ),
        migrations.RemoveField(
            model_name='matchpreferencedata',
            name='user',
        ),
        migrations.DeleteModel(
            name='MatchPreferenceData',
        ),
        migrations.RemoveField(
            model_name='preferenceoptions',
            name='match_function',
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
        migrations.DeleteModel(
            name='PreferenceOptions',
        ),
        migrations.DeleteModel(
            name='Similarity',
        ),
        migrations.DeleteModel(
            name='SimilarityData',
        ),
        migrations.RemoveField(
            model_name='userfilterdata',
            name='filter',
        ),
        migrations.RemoveField(
            model_name='userfilterdata',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserFilterData',
        ),
        migrations.RemoveField(
            model_name='userpreferencedata',
            name='filter',
        ),
        migrations.RemoveField(
            model_name='userpreferencedata',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserPreferenceData',
        ),
        migrations.AddField(
            model_name='usermfilter',
            name='m_filter',
            field=models.ForeignKey(to='app.MFilter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usermfilter',
            name='user',
            field=models.ForeignKey(related_name='m_filters', to='app.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mfilteroptions',
            name='matching_function',
            field=models.ForeignKey(related_name='options', to='app.MFilter'),
            preserve_default=True,
        ),
    ]
