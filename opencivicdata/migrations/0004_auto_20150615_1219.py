# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0003_auto_20150507_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='valid_through',
            field=models.CharField(null=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='bill',
            name='from_organization',
            field=models.ForeignKey(null=True, related_name='bills', to='opencivicdata.Organization'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='legislative_session',
            field=models.ForeignKey(related_name='bills', to='opencivicdata.LegislativeSession'),
        ),
        migrations.AlterField(
            model_name='billabstract',
            name='bill',
            field=models.ForeignKey(related_name='abstracts', to='opencivicdata.Bill'),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='bill',
            field=models.ForeignKey(related_name='actions', to='opencivicdata.Bill'),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='organization',
            field=models.ForeignKey(related_name='actions', to='opencivicdata.Organization'),
        ),
        migrations.AlterField(
            model_name='billactionrelatedentity',
            name='action',
            field=models.ForeignKey(related_name='related_entities', to='opencivicdata.BillAction'),
        ),
        migrations.AlterField(
            model_name='billdocument',
            name='bill',
            field=models.ForeignKey(related_name='documents', to='opencivicdata.Bill'),
        ),
        migrations.AlterField(
            model_name='billdocumentlink',
            name='document',
            field=models.ForeignKey(related_name='links', to='opencivicdata.BillDocument'),
        ),
        migrations.AlterField(
            model_name='billidentifier',
            name='bill',
            field=models.ForeignKey(related_name='other_identifiers', to='opencivicdata.Bill'),
        ),
        migrations.AlterField(
            model_name='billsource',
            name='bill',
            field=models.ForeignKey(related_name='sources', to='opencivicdata.Bill'),
        ),
        migrations.AlterField(
            model_name='billsponsorship',
            name='bill',
            field=models.ForeignKey(related_name='sponsorships', to='opencivicdata.Bill'),
        ),
        migrations.AlterField(
            model_name='billtitle',
            name='bill',
            field=models.ForeignKey(related_name='other_titles', to='opencivicdata.Bill'),
        ),
        migrations.AlterField(
            model_name='billversion',
            name='bill',
            field=models.ForeignKey(related_name='versions', to='opencivicdata.Bill'),
        ),
        migrations.AlterField(
            model_name='billversionlink',
            name='version',
            field=models.ForeignKey(related_name='links', to='opencivicdata.BillVersion'),
        ),
        migrations.AlterField(
            model_name='event',
            name='jurisdiction',
            field=models.ForeignKey(related_name='events', to='opencivicdata.Jurisdiction'),
        ),
        migrations.AlterField(
            model_name='eventagendaitem',
            name='event',
            field=models.ForeignKey(related_name='agenda', to='opencivicdata.Event'),
        ),
        migrations.AlterField(
            model_name='eventagendamedia',
            name='agenda_item',
            field=models.ForeignKey(related_name='media', to='opencivicdata.EventAgendaItem'),
        ),
        migrations.AlterField(
            model_name='eventagendamedialink',
            name='media',
            field=models.ForeignKey(related_name='links', to='opencivicdata.EventAgendaMedia'),
        ),
        migrations.AlterField(
            model_name='eventdocument',
            name='event',
            field=models.ForeignKey(related_name='documents', to='opencivicdata.Event'),
        ),
        migrations.AlterField(
            model_name='eventdocumentlink',
            name='document',
            field=models.ForeignKey(related_name='links', to='opencivicdata.EventDocument'),
        ),
        migrations.AlterField(
            model_name='eventlink',
            name='event',
            field=models.ForeignKey(related_name='links', to='opencivicdata.Event'),
        ),
        migrations.AlterField(
            model_name='eventlocation',
            name='jurisdiction',
            field=models.ForeignKey(related_name='event_locations', to='opencivicdata.Jurisdiction'),
        ),
        migrations.AlterField(
            model_name='eventmedia',
            name='event',
            field=models.ForeignKey(related_name='media', to='opencivicdata.Event'),
        ),
        migrations.AlterField(
            model_name='eventmedialink',
            name='media',
            field=models.ForeignKey(related_name='links', to='opencivicdata.EventMedia'),
        ),
        migrations.AlterField(
            model_name='eventparticipant',
            name='event',
            field=models.ForeignKey(related_name='participants', to='opencivicdata.Event'),
        ),
        migrations.AlterField(
            model_name='eventrelatedentity',
            name='agenda_item',
            field=models.ForeignKey(related_name='related_entities', to='opencivicdata.EventAgendaItem'),
        ),
        migrations.AlterField(
            model_name='eventsource',
            name='event',
            field=models.ForeignKey(related_name='sources', to='opencivicdata.Event'),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='division',
            field=models.ForeignKey(related_name='jurisdictions', to='opencivicdata.Division'),
        ),
        migrations.AlterField(
            model_name='legislativesession',
            name='classification',
            field=models.CharField(choices=[('primary', 'Primary'), ('special', 'Special')], blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='legislativesession',
            name='jurisdiction',
            field=models.ForeignKey(related_name='legislative_sessions', to='opencivicdata.Jurisdiction'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='on_behalf_of',
            field=models.ForeignKey(null=True, related_name='memberships_on_behalf_of', to='opencivicdata.Organization'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(related_name='memberships', to='opencivicdata.Organization'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(related_name='memberships', to='opencivicdata.Person'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(null=True, related_name='memberships', to='opencivicdata.Post'),
        ),
        migrations.AlterField(
            model_name='membershipcontactdetail',
            name='membership',
            field=models.ForeignKey(related_name='contact_details', to='opencivicdata.Membership'),
        ),
        migrations.AlterField(
            model_name='membershiplink',
            name='membership',
            field=models.ForeignKey(related_name='links', to='opencivicdata.Membership'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='jurisdiction',
            field=models.ForeignKey(null=True, related_name='organizations', to='opencivicdata.Jurisdiction'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='parent',
            field=models.ForeignKey(null=True, related_name='children', to='opencivicdata.Organization'),
        ),
        migrations.AlterField(
            model_name='organizationcontactdetail',
            name='organization',
            field=models.ForeignKey(related_name='contact_details', to='opencivicdata.Organization'),
        ),
        migrations.AlterField(
            model_name='organizationidentifier',
            name='organization',
            field=models.ForeignKey(related_name='identifiers', to='opencivicdata.Organization'),
        ),
        migrations.AlterField(
            model_name='organizationlink',
            name='organization',
            field=models.ForeignKey(related_name='links', to='opencivicdata.Organization'),
        ),
        migrations.AlterField(
            model_name='organizationname',
            name='end_date',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='organizationname',
            name='organization',
            field=models.ForeignKey(related_name='other_names', to='opencivicdata.Organization'),
        ),
        migrations.AlterField(
            model_name='organizationname',
            name='start_date',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='organizationsource',
            name='organization',
            field=models.ForeignKey(related_name='sources', to='opencivicdata.Organization'),
        ),
        migrations.AlterField(
            model_name='person',
            name='biography',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='national_identity',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='person',
            name='summary',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='personcontactdetail',
            name='person',
            field=models.ForeignKey(related_name='contact_details', to='opencivicdata.Person'),
        ),
        migrations.AlterField(
            model_name='personidentifier',
            name='person',
            field=models.ForeignKey(related_name='identifiers', to='opencivicdata.Person'),
        ),
        migrations.AlterField(
            model_name='personlink',
            name='person',
            field=models.ForeignKey(related_name='links', to='opencivicdata.Person'),
        ),
        migrations.AlterField(
            model_name='personname',
            name='end_date',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='personname',
            name='person',
            field=models.ForeignKey(related_name='other_names', to='opencivicdata.Person'),
        ),
        migrations.AlterField(
            model_name='personname',
            name='start_date',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='personsource',
            name='person',
            field=models.ForeignKey(related_name='sources', to='opencivicdata.Person'),
        ),
        migrations.AlterField(
            model_name='personvote',
            name='vote',
            field=models.ForeignKey(related_name='votes', to='opencivicdata.VoteEvent'),
        ),
        migrations.AlterField(
            model_name='personvote',
            name='voter',
            field=models.ForeignKey(null=True, related_name='votes', to='opencivicdata.Person'),
        ),
        migrations.AlterField(
            model_name='post',
            name='division',
            field=models.ForeignKey(default=None, null=True, related_name='posts', to='opencivicdata.Division'),
        ),
        migrations.AlterField(
            model_name='post',
            name='end_date',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='organization',
            field=models.ForeignKey(related_name='posts', to='opencivicdata.Organization'),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_date',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='postcontactdetail',
            name='post',
            field=models.ForeignKey(related_name='contact_details', to='opencivicdata.Post'),
        ),
        migrations.AlterField(
            model_name='postlink',
            name='post',
            field=models.ForeignKey(related_name='links', to='opencivicdata.Post'),
        ),
        migrations.AlterField(
            model_name='relatedbill',
            name='bill',
            field=models.ForeignKey(related_name='related_bills', to='opencivicdata.Bill'),
        ),
        migrations.AlterField(
            model_name='relatedbill',
            name='related_bill',
            field=models.ForeignKey(null=True, related_name='related_bills_reverse', to='opencivicdata.Bill'),
        ),
        migrations.AlterField(
            model_name='votecount',
            name='vote',
            field=models.ForeignKey(related_name='counts', to='opencivicdata.VoteEvent'),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='bill',
            field=models.ForeignKey(null=True, related_name='votes', to='opencivicdata.Bill'),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='legislative_session',
            field=models.ForeignKey(related_name='votes', to='opencivicdata.LegislativeSession'),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='organization',
            field=models.ForeignKey(related_name='votes', to='opencivicdata.Organization'),
        ),
        migrations.AlterField(
            model_name='votesource',
            name='vote_event',
            field=models.ForeignKey(related_name='sources', to='opencivicdata.VoteEvent'),
        ),
    ]
