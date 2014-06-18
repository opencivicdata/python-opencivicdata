# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0040_auto_20140618_0859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voteevent',
            old_name='outcome',
            new_name='result',
        ),
        migrations.RenameField(
            model_name='votesource',
            old_name='person',
            new_name='vote_event',
        ),
        migrations.AlterField(
            model_name='votecount',
            name='option',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired')], max_length=50),
        ),
        migrations.AlterField(
            model_name='personvote',
            name='option',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired')], max_length=50),
        ),
    ]
