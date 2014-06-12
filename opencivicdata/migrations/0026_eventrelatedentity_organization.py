# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0025_eventrelatedentity_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventrelatedentity',
            name='organization',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
    ]
