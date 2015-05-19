# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='classification',
            field=django.contrib.postgres.fields.ArrayField(default=list, blank=True, base_field=models.TextField(), size=None),
        ),
        migrations.AlterField(
            model_name='bill',
            name='subject',
            field=django.contrib.postgres.fields.ArrayField(default=list, base_field=models.TextField(), size=None),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='classification',
            field=django.contrib.postgres.fields.ArrayField(default=list, blank=True, base_field=models.TextField(), size=None),
        ),
        migrations.AlterField(
            model_name='eventagendaitem',
            name='notes',
            field=django.contrib.postgres.fields.ArrayField(default=list, blank=True, base_field=models.TextField(), size=None),
        ),
        migrations.AlterField(
            model_name='eventagendaitem',
            name='subjects',
            field=django.contrib.postgres.fields.ArrayField(default=list, blank=True, base_field=models.TextField(), size=None),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='feature_flags',
            field=django.contrib.postgres.fields.ArrayField(default=list, blank=True, base_field=models.TextField(), size=None),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='motion_classification',
            field=django.contrib.postgres.fields.ArrayField(default=list, blank=True, base_field=models.TextField(), size=None),
        ),
    ]
