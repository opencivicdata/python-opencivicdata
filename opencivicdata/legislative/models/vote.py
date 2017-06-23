from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.encoding import python_2_unicode_compatible

from opencivicdata.core.models.base import OCDBase, LinkBase, OCDIDField, RelatedBase
from opencivicdata.core.models import Organization, Person
from .session import LegislativeSession
from .bill import Bill, BillAction
from ... import common


@python_2_unicode_compatible
class VoteEvent(OCDBase):
    id = OCDIDField(ocd_type='vote')
    identifier = models.CharField(max_length=300, blank=True)
    motion_text = models.TextField()
    # enum
    motion_classification = ArrayField(base_field=models.TextField(), blank=True, default=list)
    start_date = models.CharField(max_length=25)                # YYYY-MM-DD HH:MM:SS+HH:MM
    end_date = models.CharField(max_length=25, blank=True)      # YYYY-MM-DD HH:MM:SS+HH:MM

    result = models.CharField(max_length=50, choices=common.VOTE_RESULT_CHOICES)
    organization = models.ForeignKey(Organization, related_name='votes')
    legislative_session = models.ForeignKey(LegislativeSession, related_name='votes')
    bill = models.ForeignKey(Bill, related_name='votes', null=True)
    bill_action = models.OneToOneField(BillAction, related_name='vote', null=True, default=None)

    def __str__(self):
        if self.identifier:
            return '{} in {}'.format(self.identifier, self.legislative_session)
        else:
            return '{} on {}'.format(self.motion_text, self.bill)

    class Meta:
        db_table = 'opencivicdata_voteevent'
        index_together = [
            ['legislative_session', 'identifier', 'bill'],
            ['legislative_session', 'bill']
        ]


@python_2_unicode_compatible
class VoteCount(RelatedBase):
    vote_event = models.ForeignKey(VoteEvent, related_name='counts')
    option = models.CharField(max_length=50, choices=common.VOTE_OPTION_CHOICES)
    value = models.PositiveIntegerField()

    def __str__(self):
        return '{0} for {1}'.format(self.value, self.option)

    class Meta:
        db_table = 'opencivicdata_votecount'


@python_2_unicode_compatible
class PersonVote(RelatedBase):
    vote_event = models.ForeignKey(VoteEvent, related_name='votes')
    option = models.CharField(max_length=50, choices=common.VOTE_OPTION_CHOICES)
    voter_name = models.CharField(max_length=300)
    voter = models.ForeignKey(Person, related_name='votes', null=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return '{0} voted for {1}'.format(self.voter_name, self.option)

    class Meta:
        db_table = 'opencivicdata_personvote'


class VoteSource(LinkBase):
    vote_event = models.ForeignKey(VoteEvent, related_name='sources')

    class Meta:
        db_table = 'opencivicdata_votesource'
