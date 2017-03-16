#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Election-related models.
"""
from __future__ import unicode_literals
import warnings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from opencivicdata.models import Event, Division
from opencivicdata.models.base import 
    IdentifierBase,
    LinkBase,
    OCDIDField,
    OCDBase,
)
from opencivicdata.models.elections import CandidateContest
from opencivicdata.models.people_orgs import (
    Organization,
    Post,
)


class Election(Event):
    """
    A collection of political contests set to be decided on the same date within a Division.
    """
    division = models.ForeignKey(
        Division,
        related_name="elections",
        help_text="Reference to the Division that defines the broadest political "
                  "geography of any contest to be decided by the election.",
    )
    administrative_org = models.ForeignKey(
        Organization,
        related_name='elections',
        null=True,
        help_text='Reference to the Organization that administers the election.',
    )

    class Meta(Event.Meta):
        """
        Model options.
        """
        ordering = ("-start_time",)


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

    def __str__(self):
        tmpl = '%s identifies %s'
        return tmpl % (self.identifier, self.election)


@python_2_unicode_compatible
class Candidacy(OCDBase):
    """
    A person competing in an election contest to hold a specific office for a term.
    """
    id = OCDIDField(
        ocd_type='candidacy',
        help_text='Open Civic Data-style id in the format ``ocd-candidacy/{{uuid}}``.',
    )
    person = models.ForeignKey(
        Person,
        related_name='candidacies',
        help_text='Reference to the Person who is the candidate.',
    )
    post = models.ForeignKey(
        Post,
        related_name='candidacies',
        help_text='Reference to Post represents the public office for which '
                  'the candidate is competing.',
    )
    contest = models.ForeignKey(
        CandidateContest,
        related_name='candidacies',
        help_text="Reference to an OCD CandidateContest representing the contest "
                  "in which the candidate is competing.",
    )
    candidate_name = models.CharField(
        max_length=300,
        help_text="For preserving the candidate's name as it was of the candidacy."
    )
    filed_date = models.DateField(
        null=True,
        help_text="Specifies when the candidate filed for the contest.",
    )
    is_incumbent = models.NullBooleanField(
        help_text="Indicates whether the candidate is seeking re-election to a "
                  "public office he/she currently holds",
    )
    party = models.ForeignKey(
        Party,
        related_name='candidacies',
        null=True,
        help_text='Reference to and Party with which the candidate is affiliated.'
    )
    top_ticket_candidacy = models.ForeignKey(
        'self',
        related_name="ticket",
        null=True,
        help_text="If the candidate is running as part of ticket, e.g., a Vice "
                  "Presidential candidate running with a Presidential candidate, "
                  "reference to candidacy at the top of the ticket."
    )

    class Meta:
        """
        Model options.
        """
        verbose_name_plural = "candidacies"
        ordering = ("contest", "post", "person",)

    def __str__(self):
        return self.ballot_name

    @property
    def election(self):
        """
        Returns the election this candidacy is tied to.
        """
        return self.contest.election


class CandidacySource(LinkBase):
    """
    Source used in assembling the Candidacy.
    """
    candidacy = models.ForeignKey(
        Candidacy,
        related_name='sources',
        help_text="Reference to the assembed Candidacy.",
    )


class Party(Organization):
    """
    A political party with which office holders and candidates may be affiliated.
    """
    abbreviation = models.CharField(
        max_length=3,
        unique=True,
        help_text='An abbreviation for the party name.',
    )
    color = models.CharField(
        max_length=6,
        blank=True,
        help_text='Six-character hex code representing an HTML color string. '
                  'The pattern is ``[0-9a-f]{6}``.',
    )
    is_write_in = models.NullBooleanField(
        null=True,
        help_text='Indicates that the party is not officially recognized by a '
                  'local, state, or federal organization but, rather, is a '
                  '"write-in" in jurisdictions which allow candidates to free-'
                  'form enter their political affiliation.',
    )

    class Meta:
        """
        Model options.
        """
        verbose_name_plural = 'parties'
        ordering = ("name",)
