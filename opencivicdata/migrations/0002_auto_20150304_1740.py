# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import uuidfield.fields
import opencivicdata.models.base
import django.core.validators


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
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='disclosure', validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-disclosure/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-disclosure/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False)),
                ('name', models.CharField(max_length=300)),
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
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='source_identified',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='from_organization',
            field=models.ForeignKey(related_name='bills', null=True, to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bill',
            name='legislative_session',
            field=models.ForeignKey(to='opencivicdata.LegislativeSession', related_name='bills'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billabstract',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='abstracts'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billaction',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='actions'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billaction',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='actions'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billactionrelatedentity',
            name='action',
            field=models.ForeignKey(to='opencivicdata.BillAction', related_name='related_entities'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billdocument',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='documents'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billdocumentlink',
            name='document',
            field=models.ForeignKey(to='opencivicdata.BillDocument', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billidentifier',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='other_identifiers'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billsource',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='sources'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billsponsorship',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='sponsorships'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billtitle',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='other_titles'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billversion',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='versions'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billversionlink',
            name='version',
            field=models.ForeignKey(to='opencivicdata.BillVersion', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='events'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventagendaitem',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='agenda'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventagendamedia',
            name='agenda_item',
            field=models.ForeignKey(to='opencivicdata.EventAgendaItem', related_name='media'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventagendamedialink',
            name='media',
            field=models.ForeignKey(to='opencivicdata.EventAgendaMedia', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventdocument',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='documents'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventdocumentlink',
            name='document',
            field=models.ForeignKey(to='opencivicdata.EventDocument', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventlink',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventlocation',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='event_locations'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventmedia',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='media'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventmedialink',
            name='media',
            field=models.ForeignKey(to='opencivicdata.EventMedia', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='participants'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventrelatedentity',
            name='agenda_item',
            field=models.ForeignKey(to='opencivicdata.EventAgendaItem', related_name='related_entities'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventsource',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='sources'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='division',
            field=models.ForeignKey(to='opencivicdata.Division', related_name='jurisdictions'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='legislativesession',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='legislative_sessions'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='on_behalf_of',
            field=models.ForeignKey(related_name='memberships_on_behalf_of', null=True, to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='memberships'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='memberships'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(related_name='memberships', null=True, to='opencivicdata.Post'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membershipcontactdetail',
            name='membership',
            field=models.ForeignKey(to='opencivicdata.Membership', related_name='contact_details'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membershiplink',
            name='membership',
            field=models.ForeignKey(to='opencivicdata.Membership', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='classification',
            field=models.CharField(max_length=100, blank=True, choices=[('legislature', 'Legislature'), ('executive', 'Executive'), ('upper', 'Upper Chamber'), ('lower', 'Lower Chamber'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission'), ('office', 'Office'), ('company', 'Company')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='jurisdiction',
            field=models.ForeignKey(related_name='organizations', null=True, to='opencivicdata.Jurisdiction'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='parent',
            field=models.ForeignKey(related_name='children', null=True, to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizationcontactdetail',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='contact_details'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizationidentifier',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='identifiers'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizationlink',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizationname',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='other_names'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizationsource',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='sources'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personcontactdetail',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='contact_details'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personidentifier',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='identifiers'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personlink',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personname',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='other_names'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personsource',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='sources'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personvote',
            name='vote',
            field=models.ForeignKey(to='opencivicdata.VoteEvent', related_name='votes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personvote',
            name='voter',
            field=models.ForeignKey(related_name='votes', null=True, to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='division',
            field=models.ForeignKey(related_name='posts', default=None, null=True, to='opencivicdata.Division'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='posts'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postcontactdetail',
            name='post',
            field=models.ForeignKey(to='opencivicdata.Post', related_name='contact_details'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postlink',
            name='post',
            field=models.ForeignKey(to='opencivicdata.Post', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relatedbill',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='related_bills'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relatedbill',
            name='related_bill',
            field=models.ForeignKey(related_name='related_bills_reverse', null=True, to='opencivicdata.Bill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='votecount',
            name='vote',
            field=models.ForeignKey(to='opencivicdata.VoteEvent', related_name='counts'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='bill',
            field=models.ForeignKey(related_name='votes', null=True, to='opencivicdata.Bill'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='legislative_session',
            field=models.ForeignKey(to='opencivicdata.LegislativeSession', related_name='votes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='votes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='votesource',
            name='vote_event',
            field=models.ForeignKey(to='opencivicdata.VoteEvent', related_name='sources'),
            preserve_default=True,
        ),
    ]
