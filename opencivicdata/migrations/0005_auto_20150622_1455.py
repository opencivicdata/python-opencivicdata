# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0004_auto_20150610_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='from_organization',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization', related_name='bills'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='legislative_session',
            field=models.ForeignKey(to='opencivicdata.LegislativeSession', related_name='bills'),
        ),
        migrations.AlterField(
            model_name='billabstract',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='abstracts'),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='actions'),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='actions'),
        ),
        migrations.AlterField(
            model_name='billactionrelatedentity',
            name='action',
            field=models.ForeignKey(to='opencivicdata.BillAction', related_name='related_entities'),
        ),
        migrations.AlterField(
            model_name='billdocument',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='documents'),
        ),
        migrations.AlterField(
            model_name='billdocumentlink',
            name='document',
            field=models.ForeignKey(to='opencivicdata.BillDocument', related_name='links'),
        ),
        migrations.AlterField(
            model_name='billidentifier',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='other_identifiers'),
        ),
        migrations.AlterField(
            model_name='billsource',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='sources'),
        ),
        migrations.AlterField(
            model_name='billsponsorship',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='sponsorships'),
        ),
        migrations.AlterField(
            model_name='billtitle',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='other_titles'),
        ),
        migrations.AlterField(
            model_name='billversion',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='versions'),
        ),
        migrations.AlterField(
            model_name='billversionlink',
            name='version',
            field=models.ForeignKey(to='opencivicdata.BillVersion', related_name='links'),
        ),
        migrations.AlterField(
            model_name='event',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='events'),
        ),
        migrations.AlterField(
            model_name='eventagendaitem',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='agenda'),
        ),
        migrations.AlterField(
            model_name='eventagendamedia',
            name='agenda_item',
            field=models.ForeignKey(to='opencivicdata.EventAgendaItem', related_name='media'),
        ),
        migrations.AlterField(
            model_name='eventagendamedialink',
            name='media',
            field=models.ForeignKey(to='opencivicdata.EventAgendaMedia', related_name='links'),
        ),
        migrations.AlterField(
            model_name='eventdocument',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='documents'),
        ),
        migrations.AlterField(
            model_name='eventdocumentlink',
            name='document',
            field=models.ForeignKey(to='opencivicdata.EventDocument', related_name='links'),
        ),
        migrations.AlterField(
            model_name='eventlink',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='links'),
        ),
        migrations.AlterField(
            model_name='eventlocation',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='event_locations'),
        ),
        migrations.AlterField(
            model_name='eventmedia',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='media'),
        ),
        migrations.AlterField(
            model_name='eventmedialink',
            name='media',
            field=models.ForeignKey(to='opencivicdata.EventMedia', related_name='links'),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='participants'),
        ),
        migrations.AlterField(
            model_name='eventrelatedentity',
            name='agenda_item',
            field=models.ForeignKey(to='opencivicdata.EventAgendaItem', related_name='related_entities'),
        ),
        migrations.AlterField(
            model_name='eventsource',
            name='event',
            field=models.ForeignKey(to='opencivicdata.Event', related_name='sources'),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='division',
            field=models.ForeignKey(to='opencivicdata.Division', related_name='jurisdictions'),
        ),
        migrations.AlterField(
            model_name='legislativesession',
            name='classification',
            field=models.CharField(max_length=100, choices=[('primary', 'Primary'), ('special', 'Special')], blank=True),
        ),
        migrations.AlterField(
            model_name='legislativesession',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='legislative_sessions'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='on_behalf_of',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization', related_name='memberships_on_behalf_of'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='memberships'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='memberships'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(null=True, to='opencivicdata.Post', related_name='memberships'),
        ),
        migrations.AlterField(
            model_name='membershipcontactdetail',
            name='membership',
            field=models.ForeignKey(to='opencivicdata.Membership', related_name='contact_details'),
        ),
        migrations.AlterField(
            model_name='membershiplink',
            name='membership',
            field=models.ForeignKey(to='opencivicdata.Membership', related_name='links'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='jurisdiction',
            field=models.ForeignKey(null=True, to='opencivicdata.Jurisdiction', related_name='organizations'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='parent',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization', related_name='children'),
        ),
        migrations.AlterField(
            model_name='organizationcontactdetail',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='contact_details'),
        ),
        migrations.AlterField(
            model_name='organizationidentifier',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='identifiers'),
        ),
        migrations.AlterField(
            model_name='organizationlink',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='links'),
        ),
        migrations.AlterField(
            model_name='organizationname',
            name='end_date',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='organizationname',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='other_names'),
        ),
        migrations.AlterField(
            model_name='organizationname',
            name='start_date',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='organizationsource',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='sources'),
        ),
        migrations.AlterField(
            model_name='person',
            name='biography',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='national_identity',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='summary',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='personcontactdetail',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='contact_details'),
        ),
        migrations.AlterField(
            model_name='personidentifier',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='identifiers'),
        ),
        migrations.AlterField(
            model_name='personlink',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='links'),
        ),
        migrations.AlterField(
            model_name='personname',
            name='end_date',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='personname',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='other_names'),
        ),
        migrations.AlterField(
            model_name='personname',
            name='start_date',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='personsource',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', related_name='sources'),
        ),
        migrations.AlterField(
            model_name='personvote',
            name='vote',
            field=models.ForeignKey(to='opencivicdata.VoteEvent', related_name='votes'),
        ),
        migrations.AlterField(
            model_name='personvote',
            name='voter',
            field=models.ForeignKey(null=True, to='opencivicdata.Person', related_name='votes'),
        ),
        migrations.AlterField(
            model_name='post',
            name='division',
            field=models.ForeignKey(null=True, to='opencivicdata.Division', default=None, related_name='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='end_date',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_date',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='postcontactdetail',
            name='post',
            field=models.ForeignKey(to='opencivicdata.Post', related_name='contact_details'),
        ),
        migrations.AlterField(
            model_name='postlink',
            name='post',
            field=models.ForeignKey(to='opencivicdata.Post', related_name='links'),
        ),
        migrations.AlterField(
            model_name='relatedbill',
            name='bill',
            field=models.ForeignKey(to='opencivicdata.Bill', related_name='related_bills'),
        ),
        migrations.AlterField(
            model_name='relatedbill',
            name='related_bill',
            field=models.ForeignKey(null=True, to='opencivicdata.Bill', related_name='related_bills_reverse'),
        ),
        migrations.AlterField(
            model_name='votecount',
            name='vote',
            field=models.ForeignKey(to='opencivicdata.VoteEvent', related_name='counts'),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='bill',
            field=models.ForeignKey(null=True, to='opencivicdata.Bill', related_name='votes'),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='legislative_session',
            field=models.ForeignKey(to='opencivicdata.LegislativeSession', related_name='votes'),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', related_name='votes'),
        ),
        migrations.AlterField(
            model_name='votesource',
            name='vote_event',
            field=models.ForeignKey(to='opencivicdata.VoteEvent', related_name='sources'),
        ),
    ]
