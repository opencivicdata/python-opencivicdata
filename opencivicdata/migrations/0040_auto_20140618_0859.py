# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0039_auto_20140617_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billaction',
            old_name='text',
            new_name='description',
        ),
    ]
