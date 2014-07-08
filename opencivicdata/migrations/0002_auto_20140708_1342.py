# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personvote',
            name='option',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired'), ('other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='votecount',
            name='option',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired'), ('other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='end_date',
            field=models.CharField(blank=True, max_length=19),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='start_date',
            field=models.CharField(max_length=19),
        ),
    ]
