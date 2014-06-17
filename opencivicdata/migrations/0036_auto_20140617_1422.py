# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0035_auto_20140617_1325'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BillSummary',
            new_name='BillAbstract',
        ),
        migrations.CreateModel(
            name='BillIdentifier',
            fields=[
                ('id', uuidfield.fields.UUIDField(primary_key=True, max_length=32, serialize=False, unique=True, editable=False, blank=True)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('bill', models.ForeignKey(to_field='id', to='opencivicdata.Bill')),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='billversion',
            old_name='name',
            new_name='note',
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='name',
            new_name='identifier',
        ),
        migrations.RenameField(
            model_name='billdocument',
            old_name='name',
            new_name='note',
        ),
        migrations.RenameField(
            model_name='billabstract',
            old_name='text',
            new_name='abstract',
        ),
        migrations.RenameField(
            model_name='billtitle',
            old_name='text',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='billdocument',
            name='type',
        ),
        migrations.RemoveField(
            model_name='billversion',
            name='type',
        ),
        migrations.DeleteModel(
            name='BillName',
        ),
    ]
