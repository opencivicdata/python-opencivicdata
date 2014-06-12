# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0026_eventrelatedentity_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='on_behalf_of',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
    ]
