# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields
import opencivicdata.models.base
import django.core.validators
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disclosure',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='disclosure', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-disclosure/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-disclosure/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('classification', models.CharField(max_length=100)),
                ('effective_date', models.DateTimeField()),
                ('submitted_date', models.DateTimeField()),
                ('timezone', models.CharField(max_length=300)),
                ('jurisdiction', models.ForeignKey(related_name='disclosures', to='opencivicdata.Jurisdiction')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisclosureDocument',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, unique=True, serialize=False, max_length=32, primary_key=True, blank=True)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('date', models.CharField(max_length=10)),
                ('disclosure', models.ForeignKey(related_name='documents', to='opencivicdata.Disclosure')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisclosureDocumentLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, unique=True, serialize=False, max_length=32, primary_key=True, blank=True)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('document', models.ForeignKey(related_name='links', to='opencivicdata.DisclosureDocument')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisclosureIdentifier',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, unique=True, serialize=False, max_length=32, primary_key=True, blank=True)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('disclosure', models.ForeignKey(related_name='identifiers', to='opencivicdata.Disclosure')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisclosureRelatedEntity',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, unique=True, serialize=False, max_length=32, primary_key=True, blank=True)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(max_length=20, blank=True)),
                ('note', models.TextField()),
                ('classification', models.TextField()),
                ('disclosure', models.ForeignKey(related_name='related_entities', to='opencivicdata.Disclosure')),
                ('event', models.ForeignKey(null=True, to='opencivicdata.Event')),
                ('organization', models.ForeignKey(null=True, to='opencivicdata.Organization')),
                ('person', models.ForeignKey(null=True, to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisclosureSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, unique=True, serialize=False, max_length=32, primary_key=True, blank=True)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('disclosure', models.ForeignKey(related_name='sources', to='opencivicdata.Disclosure')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterIndexTogether(
            name='disclosure',
            index_together=set([('jurisdiction', 'classification', 'effective_date')]),
        ),
    ]
