# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0005_auto_20140711_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDocumentLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, unique=True, max_length=32, primary_key=True, editable=False, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('document', models.ForeignKey(to='opencivicdata.EventDocument')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='eventdocument',
            name='date',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]
