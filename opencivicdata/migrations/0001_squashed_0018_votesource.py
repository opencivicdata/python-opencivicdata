# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import djorm_pgarray.fields
import django.contrib.gis.db.models.fields
import uuidfield.fields
import opencivicdata.models.base
import jsonfield.fields


class Migration(migrations.Migration):

    replaces = [('opencivicdata', '0001_initial'), ('opencivicdata', '0002_bill_billaction_billdocument_eventagendamedialink_personcontactdetail_personidentifier_personlink_pe'), ('opencivicdata', '0003_billdocumentlink_billname_billsource_billsummary_billtitle_billversion'), ('opencivicdata', '0004_billactionrelatedentity_billsponsor_billversionlink_division_jurisdiction_relatedbill'), ('opencivicdata', '0005_eventlocation'), ('opencivicdata', '0006_event'), ('opencivicdata', '0007_eventdocument'), ('opencivicdata', '0008_eventlink'), ('opencivicdata', '0009_eventmedia'), ('opencivicdata', '0010_eventmedialink'), ('opencivicdata', '0011_eventsource'), ('opencivicdata', '0012_eventparticipant_eventrelatedentity_jurisdictionsession_membership_membershipcontactdetail_membershi'), ('opencivicdata', '0013_postcontactdetail'), ('opencivicdata', '0014_postlink'), ('opencivicdata', '0015_voteevent'), ('opencivicdata', '0016_personvote'), ('opencivicdata', '0017_votecount'), ('opencivicdata', '0018_votesource')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='person', serialize=False)),
                ('name', models.CharField(max_length=300)),
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
        migrations.CreateModel(
            name='EventAgendaItem',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
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
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=100)),
                ('date', models.CharField(blank=True, max_length=10)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('agenda_item', models.ForeignKey(to='opencivicdata.EventAgendaItem', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventAgendaMediaLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('mimetype', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('media', models.ForeignKey(to='opencivicdata.EventAgendaMedia', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('person', models.ForeignKey(to='opencivicdata.Person', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonIdentifier',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('person', models.ForeignKey(to='opencivicdata.Person', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('person', models.ForeignKey(to='opencivicdata.Person', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonName',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=500)),
                ('note', models.CharField(blank=True, max_length=500)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('person', models.ForeignKey(to='opencivicdata.Person', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('person', models.ForeignKey(to='opencivicdata.Person', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-bill/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='bill', serialize=False)),
                ('name', models.CharField(max_length=100)),
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
            name='BillAction',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', to_field='id')),
                ('actor', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.CharField(max_length=10)),
                ('classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('order', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillDocument',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', to_field='id')),
                ('name', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillDocumentLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('mimetype', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('document', models.ForeignKey(to='opencivicdata.BillDocument', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillName',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', to_field='id')),
                ('name', models.CharField(max_length=100)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillSummary',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', to_field='id')),
                ('text', models.TextField()),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillTitle',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', to_field='id')),
                ('text', models.TextField()),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillVersion',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', to_field='id')),
                ('name', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillVersionLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('mimetype', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('document', models.ForeignKey(to='opencivicdata.BillVersion', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelatedBill',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', to_field='id')),
                ('related_bill', models.ForeignKey(null=True, to='opencivicdata.Bill', to_field='id')),
                ('name', models.CharField(max_length=100)),
                ('session', models.CharField(max_length=100)),
                ('relation_type', models.CharField(choices=[('companion', 'Companion'), ('prior-session', 'Prior Session'), ('replaced-by', 'Replaced By'), ('replaces', 'Replaces')], max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillActionRelatedEntity',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('person', models.ForeignKey(null=True, to='opencivicdata.Person', to_field='id')),
                ('action', models.ForeignKey(to='opencivicdata.BillAction', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillSponsor',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('person', models.ForeignKey(null=True, to='opencivicdata.Person', to_field='id')),
                ('bill', models.ForeignKey(to='opencivicdata.Bill', to_field='id')),
                ('primary', models.BooleanField(default=False)),
                ('classification', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jurisdiction',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', regex='^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$', flags=32)], ocd_type='jurisdiction', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField()),
                ('classification', models.CharField(default='government', choices=[('government', 'Government'), ('school board', 'School Board')], max_length=50)),
                ('feature_flags', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('division', models.ForeignKey(to='opencivicdata.Division', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('jurisdiction', models.ForeignKey(to='opencivicdata.Jurisdiction', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='event', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('jurisdiction', models.ForeignKey(to='opencivicdata.Jurisdiction', to_field='id')),
                ('description', models.TextField()),
                ('classification', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('all_day', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('cancelled', 'Cancelled'), ('tentative', 'Tentative'), ('confirmed', 'Confirmed'), ('passed', 'Passed')], max_length=20)),
                ('location', models.ForeignKey(null=True, to='opencivicdata.EventLocation', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventDocument',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('mimetype', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('event', models.ForeignKey(to='opencivicdata.Event', to_field='id')),
                ('name', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('event', models.ForeignKey(to='opencivicdata.Event', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventMedia',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=300)),
                ('type', models.CharField(max_length=100)),
                ('date', models.CharField(blank=True, max_length=10)),
                ('offset', models.PositiveIntegerField(null=True)),
                ('event', models.ForeignKey(to='opencivicdata.Event', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventMediaLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('mimetype', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('media', models.ForeignKey(to='opencivicdata.EventMedia', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('event', models.ForeignKey(to='opencivicdata.Event', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JurisdictionSession',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('jurisdiction', models.ForeignKey(to='opencivicdata.Jurisdiction', to_field='id')),
                ('name', models.CharField(max_length=300)),
                ('classification', models.CharField(choices=[('primary', 'Primary'), ('special', 'Special')], max_length=100)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('person', models.ForeignKey(null=True, to='opencivicdata.Person', to_field='id')),
                ('event', models.ForeignKey(to='opencivicdata.Event', to_field='id')),
                ('note', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventRelatedEntity',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=300)),
                ('entity_type', models.CharField(max_length=20)),
                ('person', models.ForeignKey(null=True, to='opencivicdata.Person', to_field='id')),
                ('agenda_item', models.ForeignKey(to='opencivicdata.EventAgendaItem', to_field='id')),
                ('bill', models.ForeignKey(null=True, to='opencivicdata.Bill', to_field='id')),
                ('note', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='membership', serialize=False)),
                ('person', models.ForeignKey(to='opencivicdata.Person', to_field='id')),
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
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('membership', models.ForeignKey(to='opencivicdata.Membership', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MembershipLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('membership', models.ForeignKey(to='opencivicdata.Membership', to_field='id')),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='organization', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('image', models.URLField(blank=True)),
                ('jurisdiction', models.ForeignKey(null=True, to='opencivicdata.Jurisdiction', to_field='id')),
                ('classification', models.CharField(blank=True, choices=[('legislature', 'Legislature'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission')], max_length=100)),
                ('chamber', models.CharField(blank=True, max_length=10)),
                ('founding_date', models.CharField(blank=True, max_length=10)),
                ('dissolution_date', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationIdentifier',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationName',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('name', models.CharField(max_length=500)),
                ('note', models.CharField(blank=True, max_length=500)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrganizationSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', to_field='id')),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='post', serialize=False)),
                ('label', models.CharField(max_length=300)),
                ('role', models.CharField(blank=True, max_length=300)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', to_field='id')),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostContactDetail',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('type', models.CharField(choices=[('address', 'Postal Address'), ('email', 'Email'), ('url', 'URL'), ('fax', 'Fax'), ('text', 'Text Phone'), ('voice', 'Voice Phone'), ('video', 'Video Phone'), ('pager', 'Pager'), ('textphone', 'Device for people with hearing impairment')], max_length=50)),
                ('value', models.CharField(max_length=300)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('label', models.CharField(blank=True, max_length=300)),
                ('post', models.ForeignKey(to='opencivicdata.Post', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostLink',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('post', models.ForeignKey(to='opencivicdata.Post', to_field='id')),
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
                ('id', opencivicdata.models.base.OCDIDField(validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], ocd_type='vote', serialize=False)),
                ('identifier', models.CharField(blank=True, max_length=300)),
                ('motion', models.TextField()),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(blank=True, max_length=10)),
                ('classification', djorm_pgarray.fields.ArrayField(dbtype='text')),
                ('outcome', models.CharField(choices=[('pass', 'Pass'), ('fail', 'Fail')], max_length=50)),
                ('organization', models.ForeignKey(to='opencivicdata.Organization', to_field='id')),
                ('session', models.ForeignKey(to='opencivicdata.JurisdictionSession', to_field='id')),
                ('bill', models.ForeignKey(null=True, to='opencivicdata.Bill', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonVote',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('vote', models.ForeignKey(to='opencivicdata.VoteEvent', to_field='id')),
                ('option', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('abstain', 'Abstain'), ('paired', 'Paired')], max_length=50)),
                ('voter_name', models.CharField(max_length=300)),
                ('voter', models.ForeignKey(null=True, to='opencivicdata.Person', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteCount',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('vote', models.ForeignKey(to='opencivicdata.VoteEvent', to_field='id')),
                ('option', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('abstain', 'Abstain'), ('paired', 'Paired')], max_length=50)),
                ('value', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VoteSource',
            fields=[
                ('id', uuidfield.fields.UUIDField(max_length=32, blank=True, serialize=False, unique=True, primary_key=True, editable=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField()),
                ('person', models.ForeignKey(to='opencivicdata.VoteEvent', to_field='id')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
