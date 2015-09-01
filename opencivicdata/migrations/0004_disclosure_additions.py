# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import uuidfield.fields
import opencivicdata.models.base
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0003_auto_20150507_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disclosure',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='disclosure', validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-disclosure/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-disclosure/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('source_identified', models.NullBooleanField(default=False)),
                ('description', models.TextField()),
                ('classification', models.CharField(max_length=100)),
                ('effective_date', models.DateTimeField()),
                ('submitted_date', models.DateTimeField()),
                ('timezone', models.CharField(max_length=300)),
                ('jurisdiction', models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='disclosures')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisclosureDocument',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, max_length=32, blank=True, unique=True, primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('date', models.CharField(max_length=10)),
                ('disclosure', models.ForeignKey(to='opencivicdata.Disclosure', related_name='documents')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisclosureDocumentLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, max_length=32, blank=True, unique=True, primary_key=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('document', models.ForeignKey(to='opencivicdata.DisclosureDocument', related_name='links')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisclosureIdentifier',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, max_length=32, blank=True, unique=True, primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('disclosure', models.ForeignKey(to='opencivicdata.Disclosure', related_name='identifiers')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisclosureRelatedEntity',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, max_length=32, blank=True, unique=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(max_length=20, blank=True)),
                ('note', models.TextField()),
                ('classification', models.TextField()),
                ('disclosure', models.ForeignKey(to='opencivicdata.Disclosure', related_name='related_entities')),
                ('event', models.ForeignKey(to='opencivicdata.Event', null=True)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', null=True)),
                ('person', models.ForeignKey(to='opencivicdata.Person', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisclosureSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, max_length=32, blank=True, unique=True, primary_key=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('disclosure', models.ForeignKey(to='opencivicdata.Disclosure', related_name='sources')),
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
        migrations.AddField(
            model_name='organization',
            name='source_identified',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='source_identified',
            field=models.NullBooleanField(default=False),
        ),
    ]
