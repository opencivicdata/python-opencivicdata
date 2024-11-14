# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 18:46
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import opencivicdata.core.models.base
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Division",
            fields=[
                (
                    "id",
                    models.CharField(max_length=300, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=300)),
                ("country", models.CharField(max_length=2)),
                ("subtype1", models.CharField(blank=True, max_length=50)),
                ("subid1", models.CharField(blank=True, max_length=100)),
                ("subtype2", models.CharField(blank=True, max_length=50)),
                ("subid2", models.CharField(blank=True, max_length=100)),
                ("subtype3", models.CharField(blank=True, max_length=50)),
                ("subid3", models.CharField(blank=True, max_length=100)),
                ("subtype4", models.CharField(blank=True, max_length=50)),
                ("subid4", models.CharField(blank=True, max_length=100)),
                ("subtype5", models.CharField(blank=True, max_length=50)),
                ("subid5", models.CharField(blank=True, max_length=100)),
                ("subtype6", models.CharField(blank=True, max_length=50)),
                ("subid6", models.CharField(blank=True, max_length=100)),
                ("subtype7", models.CharField(blank=True, max_length=50)),
                ("subid7", models.CharField(blank=True, max_length=100)),
                (
                    "redirect",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.Division",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_division"},
        ),
        migrations.CreateModel(
            name="Jurisdiction",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "extras",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=dict
                    ),
                ),
                (
                    "locked_fields",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "id",
                    opencivicdata.core.models.base.OCDIDField(
                        ocd_type="jurisdiction",
                        serialize=False,
                        validators=[
                            django.core.validators.RegexValidator(
                                flags=32,
                                message="ID must match ^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$", # noqa
                                regex="^ocd-jurisdiction/country:[a-z]{2}(/[^\\W\\d]+:[\\w.~-]+)*/\\w+$", # noqa
                            )
                        ],
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                ("url", models.URLField(max_length=2000)),
                (
                    "classification",
                    models.CharField(
                        choices=[
                            ("government", "Government"),
                            ("legislature", "Legislature"),
                            ("executive", "Executive"),
                            ("school", "School System"),
                            ("park", "Park District"),
                            ("sewer", "Sewer District"),
                            ("forest", "Forest Preserve District"),
                            ("transit_authority", "Transit Authority"),
                        ],
                        db_index=True,
                        default="government",
                        max_length=50,
                    ),
                ),
                (
                    "feature_flags",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "division",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="jurisdictions",
                        to="core.Division",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_jurisdiction"},
        ),
        migrations.CreateModel(
            name="Membership",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "extras",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=dict
                    ),
                ),
                (
                    "locked_fields",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "id",
                    opencivicdata.core.models.base.OCDIDField(
                        ocd_type="membership",
                        serialize=False,
                        validators=[
                            django.core.validators.RegexValidator(
                                flags=32,
                                message="ID must match ^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$", # noqa
                                regex="^ocd-membership/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$",
                            )
                        ],
                    ),
                ),
                (
                    "person_name",
                    models.CharField(blank=True, default="", max_length=300),
                ),
                ("label", models.CharField(blank=True, max_length=300)),
                ("role", models.CharField(blank=True, max_length=300)),
                ("start_date", models.CharField(blank=True, max_length=10)),
                ("end_date", models.CharField(blank=True, max_length=10)),
            ],
            options={"db_table": "opencivicdata_membership"},
        ),
        migrations.CreateModel(
            name="MembershipContactDetail",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("address", "Postal Address"),
                            ("email", "Email"),
                            ("url", "URL"),
                            ("fax", "Fax"),
                            ("text", "Text Phone"),
                            ("voice", "Voice Phone"),
                            ("video", "Video Phone"),
                            ("pager", "Pager"),
                            ("textphone", "Device for people with hearing impairment"),
                        ],
                        max_length=50,
                    ),
                ),
                ("value", models.CharField(max_length=300)),
                ("note", models.CharField(blank=True, max_length=300)),
                ("label", models.CharField(blank=True, max_length=300)),
                (
                    "membership",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_details",
                        to="core.Membership",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_membershipcontactdetail"},
        ),
        migrations.CreateModel(
            name="MembershipLink",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("note", models.CharField(blank=True, max_length=300)),
                ("url", models.URLField(max_length=2000)),
                (
                    "membership",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="core.Membership",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_membershiplink"},
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "extras",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=dict
                    ),
                ),
                (
                    "locked_fields",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "id",
                    opencivicdata.core.models.base.OCDIDField(
                        ocd_type="organization",
                        serialize=False,
                        validators=[
                            django.core.validators.RegexValidator(
                                flags=32,
                                message="ID must match ^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$", # noqa
                                regex="^ocd-organization/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$", # noqa
                            )
                        ],
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                ("image", models.URLField(blank=True, max_length=2000)),
                (
                    "classification",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("legislature", "Legislature"),
                            ("executive", "Executive"),
                            ("upper", "Upper Chamber"),
                            ("lower", "Lower Chamber"),
                            ("party", "Party"),
                            ("committee", "Committee"),
                            ("commission", "Commission"),
                            ("corporation", "Corporation"),
                            ("agency", "Agency"),
                            ("department", "Department"),
                        ],
                        max_length=100,
                    ),
                ),
                ("founding_date", models.CharField(blank=True, max_length=10)),
                ("dissolution_date", models.CharField(blank=True, max_length=10)),
                (
                    "jurisdiction",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organizations",
                        to="core.Jurisdiction",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="core.Organization",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_organization"},
        ),
        migrations.CreateModel(
            name="OrganizationContactDetail",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("address", "Postal Address"),
                            ("email", "Email"),
                            ("url", "URL"),
                            ("fax", "Fax"),
                            ("text", "Text Phone"),
                            ("voice", "Voice Phone"),
                            ("video", "Video Phone"),
                            ("pager", "Pager"),
                            ("textphone", "Device for people with hearing impairment"),
                        ],
                        max_length=50,
                    ),
                ),
                ("value", models.CharField(max_length=300)),
                ("note", models.CharField(blank=True, max_length=300)),
                ("label", models.CharField(blank=True, max_length=300)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_details",
                        to="core.Organization",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_organizationcontactdetail"},
        ),
        migrations.CreateModel(
            name="OrganizationIdentifier",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("identifier", models.CharField(max_length=300)),
                ("scheme", models.CharField(max_length=300)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="identifiers",
                        to="core.Organization",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_organizationidentifier"},
        ),
        migrations.CreateModel(
            name="OrganizationLink",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("note", models.CharField(blank=True, max_length=300)),
                ("url", models.URLField(max_length=2000)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="core.Organization",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_organizationlink"},
        ),
        migrations.CreateModel(
            name="OrganizationName",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=500)),
                ("note", models.CharField(blank=True, max_length=500)),
                ("start_date", models.CharField(blank=True, max_length=10)),
                ("end_date", models.CharField(blank=True, max_length=10)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="other_names",
                        to="core.Organization",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_organizationname"},
        ),
        migrations.CreateModel(
            name="OrganizationSource",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("note", models.CharField(blank=True, max_length=300)),
                ("url", models.URLField(max_length=2000)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sources",
                        to="core.Organization",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_organizationsource"},
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "extras",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=dict
                    ),
                ),
                (
                    "locked_fields",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "id",
                    opencivicdata.core.models.base.OCDIDField(
                        ocd_type="person",
                        serialize=False,
                        validators=[
                            django.core.validators.RegexValidator(
                                flags=32,
                                message="ID must match ^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$", # noqa
                                regex="^ocd-person/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$",
                            )
                        ],
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=300)),
                ("sort_name", models.CharField(blank=True, default="", max_length=100)),
                ("family_name", models.CharField(blank=True, max_length=100)),
                ("given_name", models.CharField(blank=True, max_length=100)),
                ("image", models.URLField(blank=True, max_length=2000)),
                ("gender", models.CharField(blank=True, max_length=100)),
                ("summary", models.CharField(blank=True, max_length=500)),
                ("national_identity", models.CharField(blank=True, max_length=300)),
                ("biography", models.TextField(blank=True)),
                ("birth_date", models.CharField(blank=True, max_length=10)),
                ("death_date", models.CharField(blank=True, max_length=10)),
            ],
            options={
                "verbose_name_plural": "people",
                "db_table": "opencivicdata_person",
            },
        ),
        migrations.CreateModel(
            name="PersonContactDetail",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("address", "Postal Address"),
                            ("email", "Email"),
                            ("url", "URL"),
                            ("fax", "Fax"),
                            ("text", "Text Phone"),
                            ("voice", "Voice Phone"),
                            ("video", "Video Phone"),
                            ("pager", "Pager"),
                            ("textphone", "Device for people with hearing impairment"),
                        ],
                        max_length=50,
                    ),
                ),
                ("value", models.CharField(max_length=300)),
                ("note", models.CharField(blank=True, max_length=300)),
                ("label", models.CharField(blank=True, max_length=300)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_details",
                        to="core.Person",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_personcontactdetail"},
        ),
        migrations.CreateModel(
            name="PersonIdentifier",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("identifier", models.CharField(max_length=300)),
                ("scheme", models.CharField(max_length=300)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="identifiers",
                        to="core.Person",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_personidentifier"},
        ),
        migrations.CreateModel(
            name="PersonLink",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("note", models.CharField(blank=True, max_length=300)),
                ("url", models.URLField(max_length=2000)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="core.Person",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_personlink"},
        ),
        migrations.CreateModel(
            name="PersonName",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=500)),
                ("note", models.CharField(blank=True, max_length=500)),
                ("start_date", models.CharField(blank=True, max_length=10)),
                ("end_date", models.CharField(blank=True, max_length=10)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="other_names",
                        to="core.Person",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_personname"},
        ),
        migrations.CreateModel(
            name="PersonSource",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("note", models.CharField(blank=True, max_length=300)),
                ("url", models.URLField(max_length=2000)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sources",
                        to="core.Person",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_personsource"},
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "extras",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=dict
                    ),
                ),
                (
                    "locked_fields",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "id",
                    opencivicdata.core.models.base.OCDIDField(
                        ocd_type="post",
                        serialize=False,
                        validators=[
                            django.core.validators.RegexValidator(
                                flags=32,
                                message="ID must match ^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$", # noqa
                                regex="^ocd-post/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$",
                            )
                        ],
                    ),
                ),
                ("label", models.CharField(max_length=300)),
                ("role", models.CharField(blank=True, max_length=300)),
                ("start_date", models.CharField(blank=True, max_length=10)),
                ("end_date", models.CharField(blank=True, max_length=10)),
                (
                    "division",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to="core.Division",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="posts",
                        to="core.Organization",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_post"},
        ),
        migrations.CreateModel(
            name="PostContactDetail",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("address", "Postal Address"),
                            ("email", "Email"),
                            ("url", "URL"),
                            ("fax", "Fax"),
                            ("text", "Text Phone"),
                            ("voice", "Voice Phone"),
                            ("video", "Video Phone"),
                            ("pager", "Pager"),
                            ("textphone", "Device for people with hearing impairment"),
                        ],
                        max_length=50,
                    ),
                ),
                ("value", models.CharField(max_length=300)),
                ("note", models.CharField(blank=True, max_length=300)),
                ("label", models.CharField(blank=True, max_length=300)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_details",
                        to="core.Post",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_postcontactdetail"},
        ),
        migrations.CreateModel(
            name="PostLink",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("note", models.CharField(blank=True, max_length=300)),
                ("url", models.URLField(max_length=2000)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="core.Post",
                    ),
                ),
            ],
            options={"db_table": "opencivicdata_postlink"},
        ),
        migrations.AddField(
            model_name="membership",
            name="on_behalf_of",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="memberships_on_behalf_of",
                to="core.Organization",
            ),
        ),
        migrations.AddField(
            model_name="membership",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="memberships",
                to="core.Organization",
            ),
        ),
        migrations.AddField(
            model_name="membership",
            name="person",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="memberships",
                to="core.Person",
            ),
        ),
        migrations.AddField(
            model_name="membership",
            name="post",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="memberships",
                to="core.Post",
            ),
        ),
        migrations.AddIndex(
            model_name="post", index=django.db.models.Index(name="post", fields=["organization", "label"])
        ),
        migrations.AddIndex(
            model_name="organization",
            index=django.db.models.Index(name="organization_class_name", fields=["classification", "name"])
        ), 
        migrations.AddIndex(
            model_name="organization",
            index=django.db.models.Index(name="organization", fields=["jurisdiction", "classification", "name"])
        ),
        migrations.AddIndex(
            model_name="membership",
            index=django.db.models.Index(name="membership", fields=["organization", "person", "label", "post"])
        ),
    ]
