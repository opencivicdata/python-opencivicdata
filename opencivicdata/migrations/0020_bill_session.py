# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0019_bill_from_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='session',
            field=models.ForeignKey(to_field='id', to='opencivicdata.JurisdictionSession'),
            preserve_default=True,
        ),
    ]
