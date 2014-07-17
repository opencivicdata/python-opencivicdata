# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import opencivicdata.models.base
import uuidfield.fields
import django.contrib.gis.db.models.fields
import django.core.validators
import djorm_pgarray.fields
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='bill')),
                ('identifier', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('subject', djorm_pgarray.fields.ArrayField(dbtype='text')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillAbstract',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('abstract', models.TextField()),
                ('note', models.TextField(blank=True)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillAction',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('description', models.TextField()),
                ('date', models.CharField(max_length=10)),
                ('classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('order', models.PositiveIntegerField()),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillActionRelatedEntity',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(max_length=20, blank=True)),
                ('action', models.ForeignKey(to='opencivicdata.BillAction')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillDocument',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillDocumentLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('document', models.ForeignKey(to='opencivicdata.BillDocument')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillIdentifier',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('note', models.TextField(blank=True)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillSponsorship',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(max_length=20, blank=True)),
                ('primary', models.BooleanField(default=False)),
                ('classification', models.CharField(max_length=100)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillTitle',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('title', models.TextField()),
                ('note', models.TextField(blank=True)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillVersion',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillVersionLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('document', models.ForeignKey(to='opencivicdata.BillVersion')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.CharField(max_length=300, serialize=False, primary_key=True)),
                ('display_name', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=2)),
                ('subtype1', models.CharField(max_length=50, blank=True)),
                ('subid1', models.CharField(max_length=100, blank=True)),
                ('subtype2', models.CharField(max_length=50, blank=True)),
                ('subid2', models.CharField(max_length=100, blank=True)),
                ('subtype3', models.CharField(max_length=50, blank=True)),
                ('subid3', models.CharField(max_length=100, blank=True)),
                ('subtype4', models.CharField(max_length=50, blank=True)),
                ('subid4', models.CharField(max_length=100, blank=True)),
                ('subtype5', models.CharField(max_length=50, blank=True)),
                ('subid5', models.CharField(max_length=100, blank=True)),
                ('subtype6', models.CharField(max_length=50, blank=True)),
                ('subid6', models.CharField(max_length=100, blank=True)),
                ('subtype7', models.CharField(max_length=50, blank=True)),
                ('subid7', models.CharField(max_length=100, blank=True)),
                ('redirect', models.ForeignKey(to='opencivicdata.Division', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='event')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('classification', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('timezone', models.CharField(max_length=300)),
                ('end_time', models.DateTimeField(null=True)),
                ('all_day', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=20, choices=[('cancelled', 'Cancelled'), ('tentative', 'Tentative'), ('confirmed', 'Confirmed'), ('passed', 'Passed')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAgendaItem',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('description', models.TextField()),
                ('order', models.CharField(max_length=100, blank=True)),
                ('subjects', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('notes', models.TextField(blank=True)),
                ('event', models.ForeignKey(to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAgendaMedia',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10, blank=True)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('agenda_item', models.ForeignKey(to='opencivicdata.EventAgendaItem')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAgendaMediaLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('media', models.ForeignKey(to='opencivicdata.EventAgendaMedia')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventDocument',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10)),
                ('event', models.ForeignKey(to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventDocumentLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('document', models.ForeignKey(to='opencivicdata.EventDocument')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('event', models.ForeignKey(to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000, blank=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(to='opencivicdata.EventLocation', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='EventMedia',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=10, blank=True)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('event', models.ForeignKey(to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventMediaLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('media', models.ForeignKey(to='opencivicdata.EventMedia')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(max_length=20, blank=True)),
                ('note', models.TextField()),
                ('event', models.ForeignKey(to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventRelatedEntity',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(max_length=20, blank=True)),
                ('note', models.TextField()),
                ('agenda_item', models.ForeignKey(to='opencivicdata.EventAgendaItem')),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('event', models.ForeignKey(to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jurisdiction',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', flags=32, message='ID must match ^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$')], serialize=False, ocd_type='jurisdiction')),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('classification', models.CharField(max_length=50, db_index=True, choices=[('government', 'Government'), ('legislature', 'Legislature'), ('executive', 'Executive'), ('school_system', 'School System')], default='government')),
                ('feature_flags', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('division', models.ForeignKey(to='opencivicdata.Division')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='eventlocation',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='jurisdiction',
            field=models.ForeignKey(to='opencivicdata.Jurisdiction'),
            preserve_default=True,
        ),
        migrations.AlterIndexTogether(
            name='event',
            index_together=set([('jurisdiction', 'start_time', 'name')]),
        ),
        migrations.CreateModel(
            name='LegislativeSession',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('identifier', models.CharField(max_length=100)),
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
        migrations.AddField(
            model_name='bill',
            name='legislative_session',
            field=models.ForeignKey(to='opencivicdata.LegislativeSession'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='membership')),
                ('label', models.CharField(max_length=300, blank=True)),
                ('role', models.CharField(max_length=300, blank=True)),
                ('start_date', models.CharField(max_length=10, blank=True)),
                ('end_date', models.CharField(max_length=10, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MembershipContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('label', models.CharField(max_length=300, blank=True)),
                ('membership', models.ForeignKey(to='opencivicdata.Membership')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MembershipLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('membership', models.ForeignKey(to='opencivicdata.Membership')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='organization')),
                ('name', models.CharField(max_length=300)),
                ('image', models.URLField(max_length=2000, blank=True)),
                ('classification', models.CharField(max_length=100, choices=[('legislature', 'Legislature'), ('executive', 'Executive'), ('upper', 'Upper Chamber'), ('lower', 'Lower Chamber'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission')], blank=True)),
                ('founding_date', models.CharField(max_length=10, blank=True)),
                ('dissolution_date', models.CharField(max_length=10, blank=True)),
                ('jurisdiction', models.ForeignKey(to='opencivicdata.Jurisdiction', null=True)),
                ('parent', models.ForeignKey(to='opencivicdata.Organization', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='on_behalf_of',
            field=models.ForeignKey(to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billsponsorship',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billactionrelatedentity',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billaction',
            name='organization',
            field=models.ForeignKey(to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bill',
            name='from_organization',
            field=models.ForeignKey(to='opencivicdata.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AlterIndexTogether(
            name='bill',
            index_together=set([('from_organization', 'legislative_session', 'identifier')]),
        ),
        migrations.AlterIndexTogether(
            name='organization',
            index_together=set([('classification', 'name'), ('jurisdiction', 'classification', 'name')]),
        ),
        migrations.CreateModel(
            name='OrganizationContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('label', models.CharField(max_length=300, blank=True)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationIdentifier',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationName',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('note', models.CharField(max_length=500, blank=True)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='person')),
                ('name', models.CharField(max_length=300)),
                ('sort_name', models.CharField(max_length=100, default='')),
                ('image', models.URLField(max_length=2000, blank=True)),
                ('gender', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=500)),
                ('national_identity', models.CharField(max_length=300)),
                ('biography', models.TextField()),
                ('birth_date', models.CharField(max_length=10, blank=True)),
                ('death_date', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billsponsorship',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billactionrelatedentity',
            name='person',
            field=models.ForeignKey(to='opencivicdata.Person', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='PersonContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('label', models.CharField(max_length=300, blank=True)),
                ('person', models.ForeignKey(to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonIdentifier',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('person', models.ForeignKey(to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('person', models.ForeignKey(to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonName',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('note', models.CharField(max_length=500, blank=True)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('person', models.ForeignKey(to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('person', models.ForeignKey(to='opencivicdata.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonVote',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('option', models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired'), ('other', 'Other')])),
                ('voter_name', models.CharField(max_length=300)),
                ('voter', models.ForeignKey(to='opencivicdata.Person', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='post')),
                ('label', models.CharField(max_length=300)),
                ('role', models.CharField(max_length=300, blank=True)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('division', models.ForeignKey(null=True, default=None, to='opencivicdata.Division')),
                ('organization', models.ForeignKey(to='opencivicdata.Organization')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(to='opencivicdata.Post', null=True),
            preserve_default=True,
        ),
        migrations.AlterIndexTogether(
            name='membership',
            index_together=set([('organization', 'person', 'label', 'post')]),
        ),
        migrations.AlterIndexTogether(
            name='post',
            index_together=set([('organization', 'label')]),
        ),
        migrations.CreateModel(
            name='PostContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('label', models.CharField(max_length=300, blank=True)),
                ('post', models.ForeignKey(to='opencivicdata.Post')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('post', models.ForeignKey(to='opencivicdata.Post')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedBill',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('identifier', models.CharField(max_length=100)),
                ('legislative_session', models.CharField(max_length=100)),
                ('relation_type', models.CharField(max_length=100, choices=[('companion', 'Companion'), ('prior-session', 'Prior Session'), ('replaced-by', 'Replaced By'), ('replaces', 'Replaces')])),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
                ('related_bill', models.ForeignKey(to='opencivicdata.Bill', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteCount',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('option', models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired'), ('other', 'Other')])),
                ('value', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteEvent',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(regex='^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32, message='ID must match ^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='vote')),
                ('identifier', models.CharField(max_length=300, blank=True)),
                ('motion_text', models.TextField()),
                ('motion_classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('start_date', models.CharField(max_length=19)),
                ('end_date', models.CharField(max_length=19, blank=True)),
                ('result', models.CharField(max_length=50, choices=[('pass', 'Pass'), ('fail', 'Fail')])),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', null=True)),
                ('legislative_session', models.ForeignKey(to='opencivicdata.LegislativeSession')),
                ('organization', models.ForeignKey(to='opencivicdata.Organization')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='votecount',
            name='vote',
            field=models.ForeignKey(to='opencivicdata.VoteEvent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personvote',
            name='vote',
            field=models.ForeignKey(to='opencivicdata.VoteEvent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='vote',
            field=models.ForeignKey(to='opencivicdata.VoteEvent', null=True),
            preserve_default=True,
        ),
        migrations.AlterIndexTogether(
            name='voteevent',
            index_together=set([('legislative_session', 'bill'), ('legislative_session', 'identifier', 'bill')]),
        ),
        migrations.CreateModel(
            name='VoteSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(editable=False, primary_key=True, blank=True, max_length=32, unique=True, serialize=False)),
                ('note', models.CharField(max_length=300, blank=True)),
                ('url', models.URLField(max_length=2000)),
                ('vote_event', models.ForeignKey(to='opencivicdata.VoteEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
