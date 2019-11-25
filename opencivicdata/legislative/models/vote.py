from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

from opencivicdata.core.models.base import OCDBase, LinkBase, OCDIDField, RelatedBase
from opencivicdata.core.models import Organization, Person
from .session import LegislativeSession
from .bill import Bill, BillAction
from ... import common


class VoteEvent(OCDBase):
    id = OCDIDField(ocd_type="vote")
    identifier = models.CharField(max_length=300, blank=True)
    motion_text = models.TextField()
    # enum
    motion_classification = ArrayField(
        base_field=models.TextField(), blank=True, default=list
    )
    start_date = models.CharField(max_length=25)  # YYYY-MM-DD HH:MM:SS+HH:MM
    end_date = models.CharField(max_length=25, blank=True)  # YYYY-MM-DD HH:MM:SS+HH:MM

    result = models.CharField(max_length=50, choices=common.VOTE_RESULT_CHOICES)
    organization = models.ForeignKey(
        Organization,
        related_name="votes",
        # make parent org hard to protect
        on_delete=models.PROTECT,
    )
    legislative_session = models.ForeignKey(
        LegislativeSession,
        related_name="votes",
        # make legislative session hard to delete
        on_delete=models.PROTECT,
    )
    bill = models.ForeignKey(
        Bill,
        related_name="votes",
        null=True,
        # if a bill was linked, the vote isn't meaningful without it
        on_delete=models.CASCADE,
    )
    bill_action = models.OneToOneField(
        BillAction,
        related_name="vote",
        null=True,
        default=None,
        # if an action goes away - VoteEvent should stay
        on_delete=models.SET_NULL,
    )

    extras = JSONField(default=dict, blank=True)

    def __str__(self):
        if self.identifier:
            return "{} in {}".format(self.identifier, self.legislative_session)
        else:
            return "{} on {}".format(self.motion_text, self.bill)

    class Meta:
        db_table = "opencivicdata_voteevent"
        index_together = [
            ["legislative_session", "identifier", "bill"],
            ["legislative_session", "bill"],
        ]


class VoteCount(RelatedBase):
    vote_event = models.ForeignKey(
        VoteEvent, related_name="counts", on_delete=models.CASCADE
    )
    option = models.CharField(max_length=50, choices=common.VOTE_OPTION_CHOICES)
    value = models.PositiveIntegerField()

    def __str__(self):
        return "{0} for {1}".format(self.value, self.option)

    class Meta:
        db_table = "opencivicdata_votecount"


class PersonVote(RelatedBase):
    vote_event = models.ForeignKey(
        VoteEvent, related_name="votes", on_delete=models.CASCADE
    )
    option = models.CharField(max_length=50, choices=common.VOTE_OPTION_CHOICES)
    voter_name = models.CharField(max_length=300)
    voter = models.ForeignKey(
        Person,
        related_name="votes",
        null=True,
        # unresolve person if they go away
        on_delete=models.SET_NULL,
    )
    note = models.TextField(blank=True)

    def __str__(self):
        return "{0} voted for {1}".format(self.voter_name, self.option)

    class Meta:
        db_table = "opencivicdata_personvote"


class VoteSource(LinkBase):
    vote_event = models.ForeignKey(
        VoteEvent, related_name="sources", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "opencivicdata_votesource"
