# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0032_post_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='classification',
            field=djorm_pgarray.fields.ArrayField(dbtype='text'),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='classification',
            field=djorm_pgarray.fields.ArrayField(dbtype='text'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='subject',
            field=djorm_pgarray.fields.ArrayField(dbtype='text'),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='classification',
            field=djorm_pgarray.fields.ArrayField(dbtype='text'),
        ),
        migrations.AlterField(
            model_name='eventagendaitem',
            name='subjects',
            field=djorm_pgarray.fields.ArrayField(dbtype='text'),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='feature_flags',
            field=djorm_pgarray.fields.ArrayField(dbtype='text'),
        ),
    ]
