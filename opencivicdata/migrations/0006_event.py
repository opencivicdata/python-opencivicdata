# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import opencivicdata.models.base
import jsonfield.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0005_eventlocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', jsonfield.fields.JSONField(default='{}', blank=True)),
                ('id', opencivicdata.models.base.OCDIDField(ocd_type='event', validators=[django.core.validators.RegexValidator(message='ID must match ^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-event/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', flags=32)], serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('jurisdiction', models.ForeignKey(to_field='id', to='opencivicdata.Jurisdiction')),
                ('description', models.TextField()),
                ('classification', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('all_day', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=20, choices=[('cancelled', 'Cancelled'), ('tentative', 'Tentative'), ('confirmed', 'Confirmed'), ('passed', 'Passed')])),
                ('location', models.ForeignKey(to_field='id', to='opencivicdata.EventLocation', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
