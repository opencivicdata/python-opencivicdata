# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0031_person_sort_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='division',
            field=models.ForeignKey(default=None, null=True, to='opencivicdata.Division', to_field='id'),
            preserve_default=True,
        ),
    ]
