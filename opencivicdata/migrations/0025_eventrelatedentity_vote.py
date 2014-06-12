# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0024_eventparticipant_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventrelatedentity',
            name='vote',
            field=models.ForeignKey(to_field='id', to='opencivicdata.VoteEvent', null=True),
            preserve_default=True,
        ),
    ]
