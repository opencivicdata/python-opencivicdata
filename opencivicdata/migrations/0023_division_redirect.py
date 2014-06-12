# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0022_billsponsor_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='redirect',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Division', null=True),
            preserve_default=True,
        ),
    ]
