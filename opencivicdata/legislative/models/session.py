from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from opencivicdata.core.models.base import RelatedBase
from opencivicdata.core.models import Jurisdiction
from ...common import SESSION_CLASSIFICATION_CHOICES


@python_2_unicode_compatible
class LegislativeSession(RelatedBase):
    jurisdiction = models.ForeignKey(Jurisdiction, related_name='legislative_sessions')
    identifier = models.CharField(max_length=100)
    name = models.CharField(max_length=300)
    classification = models.CharField(max_length=100, choices=SESSION_CLASSIFICATION_CHOICES,
                                      blank=True)
    start_date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]
    end_date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]

    def __str__(self):
        return '{} {}'.format(self.jurisdiction, self.name)

    class Meta:
        db_table = 'opencivicdata_legislativesession'
