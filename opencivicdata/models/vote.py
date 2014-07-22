from django.db import models
from djorm_pgarray.fields import ArrayField

from .base import OCDBase, LinkBase, OCDIDField, RelatedBase
from .people_orgs import Organization, Person
from .jurisdiction import LegislativeSession
from .bill import Bill
from .. import common


class VoteEvent(OCDBase):
    id = OCDIDField(ocd_type='vote')
    identifier = models.CharField(max_length=300, blank=True)
    motion_text = models.TextField()
    motion_classification = ArrayField(dbtype="text")      # enum
    start_date = models.CharField(max_length=19)    # YYYY-MM-DD HH:MM:SS
    end_date = models.CharField(max_length=19, blank=True)    # YYYY-MM-DD

    result = models.CharField(max_length=50, choices=common.VOTE_RESULT_CHOICES)
    organization = models.ForeignKey(Organization, related_name='votes')
    legislative_session = models.ForeignKey(LegislativeSession, related_name='votes')
    bill = models.ForeignKey(Bill, related_name='votes', null=True)

    def __str__(self):
        if self.identifier:
            return '{} in {}'.format(self.identifier, self.legislative_session)
        else:
            return '{} on {}'.format(self.motion_text, self.bill)

    class Meta:
        index_together = [
            ['legislative_session', 'identifier', 'bill'],
            ['legislative_session', 'bill']
        ]

class VoteCount(RelatedBase):
    vote = models.ForeignKey(VoteEvent, related_name='counts')
    option = models.CharField(max_length=50, choices=common.VOTE_OPTION_CHOICES)
    value = models.PositiveIntegerField()


class PersonVote(RelatedBase):
    vote = models.ForeignKey(VoteEvent, related_name='votes')
    option = models.CharField(max_length=50, choices=common.VOTE_OPTION_CHOICES)
    voter_name = models.CharField(max_length=300)
    voter = models.ForeignKey(Person, related_name='votes', null=True)
    note = models.TextField(blank=True)


class VoteSource(LinkBase):
    vote_event = models.ForeignKey(VoteEvent, related_name='sources')
