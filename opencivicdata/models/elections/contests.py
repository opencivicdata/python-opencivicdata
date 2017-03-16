#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Election Contest model and its subclasses.
"""
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from opencivicdata.models.base import (
    IdentifierBase,
    LinkBase,
    OCDIDField,
    OCDBase,
)
from opencivicdata.models.division import Division
from opencivicdata.models.elections import (
    Election,
    Candidacy,
    Party,
) 
from opencivicdata.models.people_orgs import (
    Membership,
    Organization,
    Post,
)


@python_2_unicode_compatible
class ContestBase(OCDBase):
    """
    A base class for representing a specific decision set before voters in an election.

    Includes properties shared by all contest types: BallotMeasureContest, 
    CandidateContest, PartyContest and RetentionContest.
    """
    id = OCDIDField(
        ocd_type="contest",
        help_text="Open Civic Data-style id in the format ``ocd-contest/{{uuid}}``.",
    )
    name = models.CharField(
        max_length=300,
        help_text="Name of the contest, not necessarily as it appears on the ballot.",
    )
    division = models.ForeignKey(
        Division,
        related_name="divisions",
        help_text="Reference to the Division that defines the political "
                  "geography of the contest, e.g., a specific Congressional or "
                  "State Senate district. Should be a subdivision of the Division "
                  "referenced by the contest's Election.",
    )
    election = models.ForeignKey(
        Election,
        related_name="contests",
        help_text="Reference to the Election in which the contest is decided.",
    )

    def __str__(self):
        return "{0} {1}".format(self.election, self.name)

    class Meta:
        """
        Model options.
        """
        ordering = ("election", "name",)


@python_2_unicode_compatible
class ContestIdentifier(IdentifierBase):
    """
    Upstream identifiers of the election, if any exist.

    For example, identfiers assigned by a Secretary of State, county or city
    elections office.
    """
    contest = models.ForeignKey(
        ContestBase,
        related_name="identifiers",
        help_text="Reference to the Contest identified by the identifier.",
    )

    def __str__(self):
        tmpl = '%s identifies %s'
        return tmpl % (self.identifier, self.contest)


class ContestSource(LinkBase):
    """
    Source used in assembling the Contest.
    """
    contest = models.ForeignKey(
        ContestBase,
        related_name='sources',
        help_text="Reference to the assembed Contest.",
    )


class BallotMeasureContest(ContestBase):
    """
    A subclass of ContestBase for representing a ballot measure before voters.
    """
    description = models.TextField(
        help_text="Text describing the purpose and/or potential outcomes of the "
                  "ballot measure, not necessarily as it appears on the ballot.",
    )
    requirement = models.CharField(
        max_length=300,
        blank=True,
        default="50% plus one vote",
        help_text="The threshold of votes the ballot measure needs in order to pass.",
    )
    classification = models.CharField(
        max_length=300,
        blank=True,
        help_text='Describes the origin and/or potential outcome of the ballot '
                  'measure, e.g., "initiative statute", "legislative constitutional '
                  'amendment".',
    )
    runoff_for_contest = models.OneToOneField(
        'self',
        related_name='runoff_contest',
        null=True,
        help_text="If this contest is a runoff to determine the outcome of a previously "
                  "undecided contest, reference to that BallotMeasureContest.",
    )


@python_2_unicode_compatible
class BallotMeasureContestOption(models.Model):
    """
    An option voters may choose in a BallotMeasureContest.
    """
    contest = models.ForeignKey(
        BallotMeasureContest,
        related_name="options",
        help_text="Reference to the BallotMeasureContest.",
    )
    text = models.CharField(
        max_length=300,
        help_text="Text of the option, not necessarily as it appears on the ballot.",
    )

    def __str__(self):
        return "{0} on {1}".format(self.text, self.contest)


class CandidateContest(ContestBase):
    """
    A subclass of ContestBase for repesenting a contest among candidates.
    """
    party = models.ForeignKey(
        Party,
        null=True,
        help_text="If the contest is among candidates of the same political party, "
                  "e.g., a partisan primary election, reference to the Party."
    )
    previous_term_unexpired = models.BooleanField(
        default=False,
        help_text="Indicates the previous public office holder vacated the post "
                  "before serving a full term."
    )
    number_elected = models.IntegerField(
        default=1,
        help_text="Number of candidates that are elected in the contest, i.e. 'N' of N-of-M."
    )
    runoff_for_contest = models.OneToOneField(
        'self',
        related_name='runoff_contest',
        null=True,
        help_text="If this contest is a runoff to determine the outcome of a "
                  "previously undecided contest, reference to that CandidateContest.",
    )


@python_2_unicode_compatible
class CandidateContestPost(models.Model):
    """
    Link between a CandidateContest and a Post at stake in the contest.
    """
    contest = models.ForeignKey(
        CandidateContest,
        related_name="posts",
        help_text="Reference to the CandidateContest in which the Post is at stake.",
    )
    post = models.ForeignKey(
        Post,
        related_name="contests",
        help_text="Reference to the Post at stake in the CandidateContest.",
    )
    sort_order = models.IntegerField(
        default=0,
        help_text="Useful for sorting for contests where two or more public offices "
                  "are at stake, e.g., in a U.S. presidential contest, the President "
                  "post would have a lower sort order than the Vice President post.",
    )

    def __str__(self):
        return "{0} in {1}".format(self.post.label, self.contest)

    @property
    def candidacies(self):
        """
        List of candidacies for the Post in the CandidateContest.
        """
        return self.contest.candidacies.filter(post=self.post)

    class Meta:
        """
        Model options.
        """
        ordering = ("contest", "sort_order",)


class PartyContest(ContestBase):
    """
    A subclass of ``Contest`` for representing a contest in which voters can vote directly for a political party.
    """
    runoff_for_contest = models.OneToOneField(
        'self',
        null=True,
        help_text="If this contest is a runoff to determine the outcome of a previously "
                  "undecided contest, reference to that PartyContest.",
    )
    

@python_2_unicode_compatible
class PartyContestOption(models.Model):
    """
    Link between a PartyContest and a Party for which a voter could vote in the election contest.
    """
    contest = models.ForeignKey(
        PartyContest,
        related_name="parties",
        help_text="Reference to the PartyContest in which the Party is an option.",
    )
    party = models.ForeignKey(
        Party,
        help_text="Reference to the Party option in the PartyContest.",
    )
    is_incumbent = models.NullBooleanField(
        help_text="Indicates whether the party currently holds majority power.",
    )

    def __str__(self):
        return "{0} in {1}".format(self.post.label, self.contest)

    class Meta:
        """
        Model options.
        """
        ordering = ("contest", "party",)


class RetentionContest(BallotMeasureContest):
    """
    A subclass of BallotMeasureContest for representing a contest where voters vote to retain or recall a current office holder.

    For example, a judicial retention or recall election.
    """
    membership = models.ForeignKey(
        Membership,
        help_text="Reference to the Membership that represents the tenure of a "
                  "person in a specific public office.",
    )
