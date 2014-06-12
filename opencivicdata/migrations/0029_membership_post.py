# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0028_membership_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Post', null=True),
            preserve_default=True,
        ),
    ]
