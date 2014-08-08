# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields
import django.core.validators
import jsonfield.fields
import django.contrib.gis.db.models.fields
import djorm_pgarray.fields
import opencivicdata.models.base


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('id', opencivicdata.models.base.OCDIDField(serialize=False, validators=[django.core.validators.RegexValidator(regex='^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='bill')),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=2000)),
                ('version', models.ForeignKey(to='opencivicdata.BillVersion')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.CharField(serialize=False, max_length=300, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=2)),
                ('subtype1', models.CharField(blank=True, max_length=50)),
                ('subid1', models.CharField(blank=True, max_length=100)),
                ('subtype2', models.CharField(blank=True, max_length=50)),
                ('subid2', models.CharField(blank=True, max_length=100)),
                ('subtype3', models.CharField(blank=True, max_length=50)),
                ('subid3', models.CharField(blank=True, max_length=100)),
                ('subtype4', models.CharField(blank=True, max_length=50)),
                ('subid4', models.CharField(blank=True, max_length=100)),
                ('subtype5', models.CharField(blank=True, max_length=50)),
                ('subid5', models.CharField(blank=True, max_length=100)),
                ('subtype6', models.CharField(blank=True, max_length=50)),
                ('subid6', models.CharField(blank=True, max_length=100)),
                ('subtype7', models.CharField(blank=True, max_length=50)),
                ('subid7', models.CharField(blank=True, max_length=100)),
                ('redirect', models.ForeignKey(null=True, to='opencivicdata.Division')),
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
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('id', opencivicdata.models.base.OCDIDField(serialize=False, validators=[django.core.validators.RegexValidator(regex='^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='event')),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('description', models.TextField()),
                ('order', models.CharField(blank=True, max_length=100)),
                ('subjects', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('notes', djorm_pgarray.fields.ArrayField(dbtype='text')),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(blank=True, max_length=10)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True, max_length=2000)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(null=True, to='opencivicdata.EventLocation'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='EventMedia',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('note', models.CharField(max_length=300)),
                ('date', models.CharField(blank=True, max_length=10)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('name', models.CharField(max_length=2000)),
                ('entity_type', models.CharField(blank=True, max_length=20)),
                ('note', models.TextField()),
                ('agenda_item', models.ForeignKey(to='opencivicdata.EventAgendaItem')),
                ('bill', models.ForeignKey(null=True, to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('id', opencivicdata.models.base.OCDIDField(serialize=False, validators=[django.core.validators.RegexValidator(regex='^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', message='ID must match ^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', flags=32)], ocd_type='jurisdiction')),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('id', opencivicdata.models.base.OCDIDField(serialize=False, validators=[django.core.validators.RegexValidator(regex='^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='membership')),
                ('label', models.CharField(blank=True, max_length=300)),
                ('role', models.CharField(blank=True, max_length=300)),
                ('start_date', models.CharField(blank=True, max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MembershipContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('id', opencivicdata.models.base.OCDIDField(serialize=False, validators=[django.core.validators.RegexValidator(regex='^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='organization')),
                ('name', models.CharField(max_length=300)),
                ('image', models.URLField(blank=True, max_length=2000)),
                ('classification', models.CharField(blank=True, max_length=100, choices=[('legislature', 'Legislature'), ('executive', 'Executive'), ('upper', 'Upper Chamber'), ('lower', 'Lower Chamber'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission')])),
                ('founding_date', models.CharField(blank=True, max_length=10)),
                ('dissolution_date', models.CharField(blank=True, max_length=10)),
                ('jurisdiction', models.ForeignKey(null=True, to='opencivicdata.Jurisdiction')),
                ('parent', models.ForeignKey(null=True, to='opencivicdata.Organization')),
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
            field=models.ForeignKey(null=True, to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventrelatedentity',
            name='organization',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='organization',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billsponsorship',
            name='organization',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billactionrelatedentity',
            name='organization',
            field=models.ForeignKey(null=True, to='opencivicdata.Organization'),
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
            field=models.ForeignKey(null=True, to='opencivicdata.Organization'),
            preserve_default=True,
        ),
        migrations.AlterIndexTogether(
            name='bill',
            index_together=set([('from_organization', 'legislative_session', 'identifier')]),
        ),
        migrations.AlterIndexTogether(
            name='organization',
            index_together=set([('jurisdiction', 'classification', 'name'), ('classification', 'name')]),
        ),
        migrations.CreateModel(
            name='OrganizationContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('name', models.CharField(max_length=500, db_index=True)),
                ('note', models.CharField(blank=True, max_length=500)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('id', opencivicdata.models.base.OCDIDField(serialize=False, validators=[django.core.validators.RegexValidator(regex='^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='person')),
                ('name', models.CharField(max_length=300, db_index=True)),
                ('sort_name', models.CharField(max_length=100, default='')),
                ('image', models.URLField(blank=True, max_length=2000)),
                ('gender', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=500)),
                ('national_identity', models.CharField(max_length=300)),
                ('biography', models.TextField()),
                ('birth_date', models.CharField(blank=True, max_length=10)),
                ('death_date', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'verbose_name_plural': 'people',
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
            field=models.ForeignKey(null=True, to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventparticipant',
            name='person',
            field=models.ForeignKey(null=True, to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billsponsorship',
            name='person',
            field=models.ForeignKey(null=True, to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='billactionrelatedentity',
            name='person',
            field=models.ForeignKey(null=True, to='opencivicdata.Person'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='PersonContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('name', models.CharField(max_length=500, db_index=True)),
                ('note', models.CharField(blank=True, max_length=500)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('option', models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired'), ('excused', 'Excused'), ('other', 'Other')])),
                ('voter_name', models.CharField(max_length=300)),
                ('note', models.TextField(blank=True)),
                ('voter', models.ForeignKey(null=True, to='opencivicdata.Person')),
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
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('id', opencivicdata.models.base.OCDIDField(serialize=False, validators=[django.core.validators.RegexValidator(regex='^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='post')),
                ('label', models.CharField(max_length=300)),
                ('role', models.CharField(blank=True, max_length=300)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('division', models.ForeignKey(null=True, to='opencivicdata.Division', default=None)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(null=True, to='opencivicdata.Post'),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('type', models.CharField(max_length=50, choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')])),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('note', models.CharField(blank=True, max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('identifier', models.CharField(max_length=100)),
                ('legislative_session', models.CharField(max_length=100)),
                ('relation_type', models.CharField(max_length=100, choices=[('companion', 'Companion'), ('prior-session', 'Prior Session'), ('replaced-by', 'Replaced By'), ('replaces', 'Replaces')])),
                ('bill', models.ForeignKey(to='opencivicdata.Bill')),
                ('related_bill', models.ForeignKey(null=True, to='opencivicdata.Bill')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteCount',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('option', models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired'), ('excused', 'Excused'), ('other', 'Other')])),
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
                ('extras', jsonfield.fields.JSONField(blank=True, default='{}')),
                ('id', opencivicdata.models.base.OCDIDField(serialize=False, validators=[django.core.validators.RegexValidator(regex='^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', message='ID must match ^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='vote')),
                ('identifier', models.CharField(blank=True, max_length=300)),
                ('motion_text', models.TextField()),
                ('motion_classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('start_date', models.CharField(max_length=19)),
                ('end_date', models.CharField(blank=True, max_length=19)),
                ('result', models.CharField(max_length=50, choices=[('pass', 'Pass'), ('fail', 'Fail')])),
                ('bill', models.ForeignKey(null=True, to='opencivicdata.Bill')),
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
            field=models.ForeignKey(null=True, to='opencivicdata.VoteEvent'),
            preserve_default=True,
        ),
        migrations.AlterIndexTogether(
            name='voteevent',
            index_together=set([('legislative_session', 'identifier', 'bill'), ('legislative_session', 'bill')]),
        ),
        migrations.CreateModel(
            name='VoteSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, primary_key=True, serialize=False, blank=True)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('vote_event', models.ForeignKey(to='opencivicdata.VoteEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
