# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0029_membership_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='parent',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
    ]
