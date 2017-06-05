#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Election-related models.
"""
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from opencivicdata.core.models.base import (
    OCDBase,
    IdentifierBase,
    LinkBase,
    OCDIDField,
)
from opencivicdata.core.models import (
    Division,
    Organization,
)


@python_2_unicode_compatible
class Election(OCDBase):
    """
    A collection of political contests set to be decided on the same date within a Division.
    """
    id = OCDIDField(
        ocd_type='election',
        help_text='Open Civic Data-style id in the format ``ocd-election/{{uuid}}``.',
    )
    name = models.CharField(
        max_length=300,
        help_text='Name of the Election.',
    )
    date = models.DateField(
        help_text="Final or only date when eligible voters may cast their "
                  "ballots in the Election. Typically this is also the same "
                  "date when results of the election's contests are first "
                  "publicly reported.",
    )
    division = models.ForeignKey(
        Division,
        related_name="elections",
        help_text="Reference to the Division that defines the broadest political "
                  "geography of any contest to be decided by the election.",
    )
    administrative_organization = models.ForeignKey(
        Organization,
        related_name='elections',
        null=True,
        help_text='Reference to the Organization that administers the election.',
    )

    def __str__(self):
        return '{0} ({1:%Y-%m-%d})'.format(self.name, self.date)

    class Meta:
        """
        Model options.
        """
        db_table = 'opencivicdata_election'
        ordering = ("-date",)


@python_2_unicode_compatible
class ElectionIdentifier(IdentifierBase):
    """
    Upstream identifiers of the election, if any exist.

    For example, identfiers assigned by a Secretary of State, county or city
    elections office.
    """
    election = models.ForeignKey(
        Election,
        related_name='identifiers',
        help_text="Reference to the Election identified by the identifier.",
    )

    class Meta:
        db_table = 'opencivicdata_electionidentifier'

    def __str__(self):
        tmpl = '%s identifies %s'
        return tmpl % (self.identifier, self.election)


class ElectionSource(LinkBase):
    event = models.ForeignKey(Election, related_name='sources')

    class Meta:
        db_table = 'opencivicdata_electionsource'
