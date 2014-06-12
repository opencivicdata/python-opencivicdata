# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0004_billactionrelatedentity_billsponsor_billversionlink_division_jurisdiction_relatedbill'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, serialize=False, primary_key=True, editable=False, max_length=32, blank=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True)),
                ('jurisdiction', models.ForeignKey(to_field='id', to='opencivicdata.Jurisdiction')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
