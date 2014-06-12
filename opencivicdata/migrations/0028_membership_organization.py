# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0027_membership_on_behalf_of'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
    ]
