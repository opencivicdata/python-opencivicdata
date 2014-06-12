# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0030_organization_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='sort_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
    ]
