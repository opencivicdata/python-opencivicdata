from django.db import models
from djorm_pgarray.fields import ArrayField

from .base import OCDBase, LinkBase, OCDIDField, RelatedBase
from .people_orgs import Organization, Person
from .jurisdiction import JurisdictionSession
from .bill import Bill
from .. import common


class VoteEvent(OCDBase):
    id = OCDIDField(ocd_type='vote')
    identifier = models.CharField(max_length=300, blank=True)
    motion = models.TextField()
    start_date = models.CharField(max_length=10)    # YYYY-MM-DD
    end_date = models.CharField(max_length=10, blank=True)    # YYYY-MM-DD

    classification = ArrayField(dbtype="text")      # enum
    outcome = models.CharField(max_length=50, choices=common.VOTE_OUTCOME_CHOICES)
    organization = models.ForeignKey(Organization, related_name='votes')
    session = models.ForeignKey(JurisdictionSession, related_name='votes')
    bill = models.ForeignKey(Bill, related_name='votes', null=True)

    def __str__(self):
        return '{} in {}'.format(self.motion, self.session)


class VoteCount(RelatedBase):
    vote = models.ForeignKey(VoteEvent, related_name='counts')
    option = models.CharField(max_length=50, choices=common.VOTE_OPTION_CHOICES)
    value = models.PositiveIntegerField()


class PersonVote(RelatedBase):
    vote = models.ForeignKey(VoteEvent, related_name='votes')
    option = models.CharField(max_length=50, choices=common.VOTE_OPTION_CHOICES)
    voter_name = models.CharField(max_length=300)
    voter = models.ForeignKey(Person, related_name='votes', null=True)


class VoteSource(LinkBase):
    person = models.ForeignKey(VoteEvent, related_name='sources')
