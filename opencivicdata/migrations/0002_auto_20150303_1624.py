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
            name='DisclosureAuthority',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, unique=True, serialize=False, max_length=32, primary_key=True, blank=True)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(max_length=20, blank=True)),
                ('disclosure', models.ForeignKey(related_name='authority', to='opencivicdata.Disclosure')),
                ('organization', models.ForeignKey(null=True, to='opencivicdata.Organization')),
                ('person', models.ForeignKey(null=True, to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
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
            name='DisclosureRegistrant',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, unique=True, serialize=False, max_length=32, primary_key=True, blank=True)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(max_length=20, blank=True)),
                ('disclosure', models.ForeignKey(related_name='registrant', to='opencivicdata.Disclosure')),
                ('organization', models.ForeignKey(null=True, to='opencivicdata.Organization')),
                ('person', models.ForeignKey(null=True, to='opencivicdata.Person')),
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
        migrations.AlterField(
            model_name='bill',
            name='from_organization',
            field=models.ForeignKey(related_name='bills', to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='legislative_session',
            field=models.ForeignKey(related_name='bills', to='opencivicdata.LegislativeSession'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billabstract',
            name='bill',
            field=models.ForeignKey(related_name='abstracts', to='opencivicdata.Bill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billaction',
            name='bill',
            field=models.ForeignKey(related_name='actions', to='opencivicdata.Bill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billaction',
            name='organization',
            field=models.ForeignKey(related_name='actions', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billactionrelatedentity',
            name='action',
            field=models.ForeignKey(related_name='related_entities', to='opencivicdata.BillAction'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billdocument',
            name='bill',
            field=models.ForeignKey(related_name='documents', to='opencivicdata.Bill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billdocumentlink',
            name='document',
            field=models.ForeignKey(related_name='links', to='opencivicdata.BillDocument'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billidentifier',
            name='bill',
            field=models.ForeignKey(related_name='other_identifiers', to='opencivicdata.Bill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billsource',
            name='bill',
            field=models.ForeignKey(related_name='sources', to='opencivicdata.Bill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billsponsorship',
            name='bill',
            field=models.ForeignKey(related_name='sponsorships', to='opencivicdata.Bill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billtitle',
            name='bill',
            field=models.ForeignKey(related_name='other_titles', to='opencivicdata.Bill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billversion',
            name='bill',
            field=models.ForeignKey(related_name='versions', to='opencivicdata.Bill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billversionlink',
            name='version',
            field=models.ForeignKey(related_name='links', to='opencivicdata.BillVersion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='jurisdiction',
            field=models.ForeignKey(related_name='events', to='opencivicdata.Jurisdiction'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventagendaitem',
            name='event',
            field=models.ForeignKey(related_name='agenda', to='opencivicdata.Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventagendamedia',
            name='agenda_item',
            field=models.ForeignKey(related_name='media', to='opencivicdata.EventAgendaItem'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventagendamedialink',
            name='media',
            field=models.ForeignKey(related_name='links', to='opencivicdata.EventAgendaMedia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventdocument',
            name='event',
            field=models.ForeignKey(related_name='documents', to='opencivicdata.Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventdocumentlink',
            name='document',
            field=models.ForeignKey(related_name='links', to='opencivicdata.EventDocument'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventlink',
            name='event',
            field=models.ForeignKey(related_name='links', to='opencivicdata.Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventlocation',
            name='jurisdiction',
            field=models.ForeignKey(related_name='event_locations', to='opencivicdata.Jurisdiction'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventmedia',
            name='event',
            field=models.ForeignKey(related_name='media', to='opencivicdata.Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventmedialink',
            name='media',
            field=models.ForeignKey(related_name='links', to='opencivicdata.EventMedia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='event',
            field=models.ForeignKey(related_name='participants', to='opencivicdata.Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventrelatedentity',
            name='agenda_item',
            field=models.ForeignKey(related_name='related_entities', to='opencivicdata.EventAgendaItem'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventsource',
            name='event',
            field=models.ForeignKey(related_name='sources', to='opencivicdata.Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='division',
            field=models.ForeignKey(related_name='jurisdictions', to='opencivicdata.Division'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='legislativesession',
            name='jurisdiction',
            field=models.ForeignKey(related_name='legislative_sessions', to='opencivicdata.Jurisdiction'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='on_behalf_of',
            field=models.ForeignKey(related_name='memberships_on_behalf_of', to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(related_name='memberships', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(related_name='memberships', to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(related_name='memberships', to='opencivicdata.Post', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membershipcontactdetail',
            name='membership',
            field=models.ForeignKey(related_name='contact_details', to='opencivicdata.Membership'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membershiplink',
            name='membership',
            field=models.ForeignKey(related_name='links', to='opencivicdata.Membership'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='classification',
            field=models.CharField(choices=[('legislature', 'Legislature'), ('executive', 'Executive'), ('upper', 'Upper Chamber'), ('lower', 'Lower Chamber'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission'), ('office', 'Office'), ('company', 'Company')], max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='jurisdiction',
            field=models.ForeignKey(related_name='organizations', to='opencivicdata.Jurisdiction', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='parent',
            field=models.ForeignKey(related_name='children', to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizationcontactdetail',
            name='organization',
            field=models.ForeignKey(related_name='contact_details', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizationidentifier',
            name='organization',
            field=models.ForeignKey(related_name='identifiers', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizationlink',
            name='organization',
            field=models.ForeignKey(related_name='links', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizationname',
            name='organization',
            field=models.ForeignKey(related_name='other_names', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizationsource',
            name='organization',
            field=models.ForeignKey(related_name='sources', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personcontactdetail',
            name='person',
            field=models.ForeignKey(related_name='contact_details', to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personidentifier',
            name='person',
            field=models.ForeignKey(related_name='identifiers', to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personlink',
            name='person',
            field=models.ForeignKey(related_name='links', to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personname',
            name='person',
            field=models.ForeignKey(related_name='other_names', to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personsource',
            name='person',
            field=models.ForeignKey(related_name='sources', to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personvote',
            name='vote',
            field=models.ForeignKey(related_name='votes', to='opencivicdata.VoteEvent'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personvote',
            name='voter',
            field=models.ForeignKey(related_name='votes', to='opencivicdata.Person', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='division',
            field=models.ForeignKey(related_name='posts', default=None, to='opencivicdata.Division', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='organization',
            field=models.ForeignKey(related_name='posts', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postcontactdetail',
            name='post',
            field=models.ForeignKey(related_name='contact_details', to='opencivicdata.Post'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postlink',
            name='post',
            field=models.ForeignKey(related_name='links', to='opencivicdata.Post'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relatedbill',
            name='bill',
            field=models.ForeignKey(related_name='related_bills', to='opencivicdata.Bill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relatedbill',
            name='related_bill',
            field=models.ForeignKey(related_name='related_bills_reverse', to='opencivicdata.Bill', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='votecount',
            name='vote',
            field=models.ForeignKey(related_name='counts', to='opencivicdata.VoteEvent'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='bill',
            field=models.ForeignKey(related_name='votes', to='opencivicdata.Bill', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='legislative_session',
            field=models.ForeignKey(related_name='votes', to='opencivicdata.LegislativeSession'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='organization',
            field=models.ForeignKey(related_name='votes', to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='votesource',
            name='vote_event',
            field=models.ForeignKey(related_name='sources', to='opencivicdata.VoteEvent'),
            preserve_default=True,
        ),
    ]
