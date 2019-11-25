#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CandidateContest-related models.
"""
from django.db import models
from opencivicdata.core.models.base import IdentifierBase, LinkBase
from opencivicdata.core.models import Organization, Post
from .base import ContestBase


class CandidateContest(ContestBase):
    """
    A contest among candidates seeking election to one or more public offices.
    """

    party = models.ForeignKey(
        Organization,
        related_name="candidate_contests",
        limit_choices_to={"classification": "party"},
        null=True,
        # survive party deletion
        on_delete=models.SET_NULL,
        help_text="If the contest is among candidates of the same political party, "
        "e.g., a partisan primary election, reference to the Organization "
        "representing that party.",
    )
    previous_term_unexpired = models.BooleanField(
        default=False,
        help_text="Indicates the previous public office holder vacated the post "
        "before serving a full term.",
    )
    number_elected = models.IntegerField(
        default=1,
        help_text="Number of candidates that are elected in the contest, i.e. 'N' of N-of-M.",
    )
    runoff_for_contest = models.OneToOneField(
        "self",
        related_name="runoff_contest",
        null=True,
        on_delete=models.SET_NULL,
        help_text="If this contest is a runoff to determine the outcome of a "
        "previously undecided contest, reference to that CandidateContest.",
    )

    class Meta(ContestBase.Meta):
        db_table = "opencivicdata_candidatecontest"


class CandidateContestPost(models.Model):
    """
    A public office (i.e., Post) at stake in a CandidateContest.
    """

    contest = models.ForeignKey(
        CandidateContest,
        related_name="posts",
        on_delete=models.CASCADE,
        help_text="Reference to the CandidateContest in which the Post is at stake.",
    )
    post = models.ForeignKey(
        Post,
        related_name="contests",
        on_delete=models.CASCADE,
        help_text="Reference to the Post representing a public office at stake in "
        "the CandidateContest.",
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
        List of candidacies for the Post in a CandidateContest.
        """
        return self.contest.candidacies.filter(post=self.post)

    class Meta:
        """
        Model options.
        """

        ordering = ("contest", "sort_order")
        db_table = "opencivicdata_candidatecontestpost"


class CandidateContestIdentifier(IdentifierBase):
    """
    Upstream identifiers of a CandidateContest.

    For example, identfiers assigned by a Secretary of State, county or city
    elections office.
    """

    contest = models.ForeignKey(
        CandidateContest,
        related_name="identifiers",
        on_delete=models.CASCADE,
        help_text="Reference to the CandidateContest linked to the upstream identifier.",
    )

    def __str__(self):
        tmpl = "%s identifies %s"
        return tmpl % (self.identifier, self.contest)

    class Meta:
        db_table = "opencivicdata_candidatecontestidentifier"


class CandidateContestSource(LinkBase):
    """
    Source used in assembling a CandidateContest.
    """

    contest = models.ForeignKey(
        CandidateContest,
        related_name="sources",
        on_delete=models.CASCADE,
        help_text="Reference to the CandidateContest assembled from the source.",
    )

    class Meta:
        db_table = "opencivicdata_candidatecontestsource"
