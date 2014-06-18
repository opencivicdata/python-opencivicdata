# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0041_auto_20140618_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voteevent',
            old_name='motion',
            new_name='motion_text',
        ),
    ]
