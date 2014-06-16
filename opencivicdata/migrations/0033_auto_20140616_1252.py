# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0032_post_division'),
    ]

    operations = [
        migrations.AddField(
            model_name='billaction',
            name='organization',
            field=models.ForeignKey(to_field='id', to='opencivicdata.Organization', default=0),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='billaction',
            name='actor',
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='classification',
            field=models.CharField(choices=[('government', 'Government'), ('legislature', 'Legislature'), ('executive', 'Executive'), ('school_system', 'School System')], default='government', max_length=50),
        ),
    ]
