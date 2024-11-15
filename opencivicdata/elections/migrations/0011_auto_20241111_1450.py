# Generated by Django 3.2 on 2024-11-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0010_auto_20221215_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ballotmeasurecontest',
            name='extras',
            field=models.JSONField(blank=True, default=dict, help_text='A key-value store for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='candidacy',
            name='extras',
            field=models.JSONField(blank=True, default=dict, help_text='A key-value store for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='candidatecontest',
            name='extras',
            field=models.JSONField(blank=True, default=dict, help_text='A key-value store for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='election',
            name='extras',
            field=models.JSONField(blank=True, default=dict, help_text='A key-value store for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='partycontest',
            name='extras',
            field=models.JSONField(blank=True, default=dict, help_text='A key-value store for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='retentioncontest',
            name='extras',
            field=models.JSONField(blank=True, default=dict, help_text='A key-value store for storing arbitrary information not covered elsewhere.'),
        ),
    ]
