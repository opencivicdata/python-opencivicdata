# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields
import django.core.validators
import django.contrib.gis.db.models.fields
import jsonfield.fields
import opencivicdata.models.base
import djorm_pgarray.fields


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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='bill')),
                ('identifier', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('subject', djorm_pgarray.fields.ArrayField(dbtype='text')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillAbstract',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('name', models.CharField(max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField()),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('name', models.CharField(max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField()),
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
                ('id', models.CharField(serialize=False, primary_key=True, max_length=300)),
                ('display_name', models.CharField(max_length=300)),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='event')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('classification', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('all_day', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('cancelled', 'Cancelled'), ('tentative', 'Tentative'), ('confirmed', 'Confirmed'), ('passed', 'Passed')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAgendaItem',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('description', models.TextField()),
                ('order', models.CharField(blank=True, max_length=100)),
                ('subjects', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAgendaMedia',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField()),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=300)),
                ('event', models.ForeignKey(to='opencivicdata.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('media_type', models.CharField(max_length=100)),
                ('url', models.URLField()),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('name', models.CharField(max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('name', models.CharField(max_length=300)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
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
                ('id', opencivicdata.models.base.OCDIDField(serialize=False, ocd_type='jurisdiction', validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', regex='^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$')])),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField()),
                ('classification', models.CharField(choices=[('government', 'Government'), ('legislature', 'Legislature'), ('executive', 'Executive'), ('school_system', 'School System')], max_length=50, default='government')),
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
        migrations.CreateModel(
            name='LegislativeSession',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('identifier', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=300)),
                ('classification', models.CharField(choices=[('primary', 'Primary'), ('special', 'Special')], max_length=100)),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='membership')),
                ('label', models.CharField(blank=True, max_length=300)),
                ('role', models.CharField(blank=True, max_length=300)),
                ('start_date', models.CharField(blank=True, max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MembershipContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='organization')),
                ('name', models.CharField(max_length=300)),
                ('image', models.URLField(blank=True)),
                ('classification', models.CharField(blank=True, choices=[('legislature', 'Legislature'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission')], max_length=100)),
                ('chamber', models.CharField(blank=True, max_length=10)),
                ('founding_date', models.CharField(blank=True, max_length=10)),
                ('dissolution_date', models.CharField(blank=True, max_length=10)),
                ('jurisdiction', models.ForeignKey(null=True, to='opencivicdata.Jurisdiction')),
                ('parent', models.ForeignKey(null=True, to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
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
        migrations.CreateModel(
            name='OrganizationContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('name', models.CharField(max_length=500)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='person')),
                ('name', models.CharField(max_length=300)),
                ('sort_name', models.CharField(max_length=100, default='')),
                ('image', models.URLField(blank=True)),
                ('gender', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=500)),
                ('national_identity', models.CharField(max_length=300)),
                ('biography', models.TextField()),
                ('birth_date', models.CharField(blank=True, max_length=10)),
                ('death_date', models.CharField(blank=True, max_length=10)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('name', models.CharField(max_length=500)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('option', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired')], max_length=50)),
                ('voter_name', models.CharField(max_length=300)),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='post')),
                ('label', models.CharField(max_length=300)),
                ('role', models.CharField(blank=True, max_length=300)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('division', models.ForeignKey(default=None, null=True, to='opencivicdata.Division')),
                ('organization', models.ForeignKey(to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(null=True, to='opencivicdata.Post'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='PostContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('identifier', models.CharField(max_length=100)),
                ('legislative_session', models.CharField(max_length=100)),
                ('relation_type', models.CharField(choices=[('companion', 'Companion'), ('prior-session', 'Prior Session'), ('replaced-by', 'Replaced By'), ('replaces', 'Replaces')], max_length=100)),
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
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('option', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('absent', 'Absent'), ('abstain', 'Abstain'), ('not voting', 'Not Voting'), ('paired', 'Paired')], max_length=50)),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')], serialize=False, ocd_type='vote')),
                ('identifier', models.CharField(blank=True, max_length=300)),
                ('motion_text', models.TextField()),
                ('motion_classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
                ('result', models.CharField(choices=[('pass', 'Pass'), ('fail', 'Fail')], max_length=50)),
                ('bill', models.ForeignKey(null=True, to='opencivicdata.Bill')),
                ('legislative_session', models.ForeignKey(to='opencivicdata.LegislativeSession')),
                ('organization', models.ForeignKey(to='opencivicdata.Organization')),
            ],
            options={
                'abstract': False,
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
        migrations.CreateModel(
            name='VoteSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(blank=True, primary_key=True, editable=False, serialize=False, unique=True, max_length=32)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('vote_event', models.ForeignKey(to='opencivicdata.VoteEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
