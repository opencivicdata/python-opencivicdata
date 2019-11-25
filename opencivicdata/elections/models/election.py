#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Election-related models.
"""
from django.db import models
from opencivicdata.core.models.base import OCDBase, IdentifierBase, LinkBase, OCDIDField
from opencivicdata.core.models import Division, Organization


class Election(OCDBase):
    """
    A collection of political contests set to be decided on the same date within a Division.
    """

    id = OCDIDField(
        ocd_type="election",
        help_text="Open Civic Data-style id in the format ``ocd-election/{{uuid}}``.",
    )
    name = models.CharField(max_length=300, help_text="Name of the Election.")
    date = models.DateField(
        help_text="Final or only date when eligible voters may cast their "
        "ballots in the Election. Typically this is also the same "
        "date when results of the election's contests are first "
        "publicly reported."
    )
    division = models.ForeignKey(
        Division,
        related_name="elections",
        help_text="Reference to the Division that defines the broadest political "
        "geography of any contest to be decided by the election.",
        # divisions should be tough to delete
        on_delete=models.PROTECT,
    )
    administrative_organization = models.ForeignKey(
        Organization,
        related_name="elections",
        null=True,
        help_text="Reference to the Organization that administers the election.",
        # shouldn't destroy election if org does go away
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return "{0} ({1:%Y-%m-%d})".format(self.name, self.date)

    class Meta:
        """
        Model options.
        """

        db_table = "opencivicdata_election"
        ordering = ("-date",)


class ElectionIdentifier(IdentifierBase):
    """
    Upstream identifiers of a Election.

    For example, identfiers assigned by a Secretary of State, county or city
    elections office.
    """

    election = models.ForeignKey(
        Election,
        related_name="identifiers",
        help_text="Reference to the Election identified by this alternative identifier.",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "opencivicdata_electionidentifier"

    def __str__(self):
        tmpl = "%s identifies %s"
        return tmpl % (self.identifier, self.election)


class ElectionSource(LinkBase):
    """
    Source used in assembling a Election.
    """

    election = models.ForeignKey(
        Election,
        related_name="sources",
        help_text="Reference to the Election this source verifies.",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "opencivicdata_electionsource"
