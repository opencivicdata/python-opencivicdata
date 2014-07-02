# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0004_auto_20140702_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegislativeSession',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, max_length=32, editable=False, serialize=False, unique=True, blank=True)),
                ('name', models.CharField(max_length=300)),
                ('classification', models.CharField(max_length=100, choices=[('primary', 'Primary'), ('special', 'Special')])),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('jurisdiction', models.ForeignKey(to='opencivicdata.Jurisdiction')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='jurisdictionsession',
            name='jurisdiction',
        ),
        migrations.DeleteModel(
            name='JurisdictionSession',
        ),
        migrations.AlterField(
            model_name='bill',
            name='legislative_session',
            field=models.ForeignKey(to='opencivicdata.LegislativeSession'),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='legislative_session',
            field=models.ForeignKey(to='opencivicdata.LegislativeSession'),
        ),
    ]
