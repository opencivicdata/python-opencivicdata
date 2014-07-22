# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'people'},
        ),
        migrations.AddField(
            model_name='personvote',
            name='note',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personvote',
            name='option',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired'), ('excused', 'Excused'), ('other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='votecount',
            name='option',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired'), ('excused', 'Excused'), ('other', 'Other')], max_length=50),
        ),
    ]
