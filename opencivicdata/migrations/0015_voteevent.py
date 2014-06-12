# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import opencivicdata.models.base
import jsonfield.fields
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0014_postlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteEvent',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='vote', validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-vote/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], serialize=False)),
                ('identifier', models.CharField(max_length=300, blank=True)),
                ('motion', models.TextField()),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10, blank=True)),
                ('classification', djorm_pgarray.fields.ArrayField(default=None, blank=True, null=True, dbtype='text')),
                ('outcome', models.CharField(max_length=50, choices=[('pass', 'Pass'), ('fail', 'Fail')])),
                ('organization', models.ForeignKey(to_field='id', to='opencivicdata.Organization')),
                ('session', models.ForeignKey(to_field='id', to='opencivicdata.JurisdictionSession')),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
