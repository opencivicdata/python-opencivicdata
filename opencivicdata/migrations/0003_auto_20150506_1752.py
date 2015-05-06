# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0002_auto_20150131_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillSummary',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, unique=True, primary_key=True, max_length=32, serialize=False, blank=True)),
                ('note', models.TextField(blank=True)),
                ('text', models.TextField()),
                ('date', models.TextField(max_length=10, blank=True)),
                ('bill', models.ForeignKey(related_name='summaries', to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
