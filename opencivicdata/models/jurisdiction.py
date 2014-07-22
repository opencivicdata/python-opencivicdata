from django.db import models
from djorm_pgarray.fields import ArrayField

from ..common import JURISDICTION_CLASSIFICATION_CHOICES, SESSION_CLASSIFICATION_CHOICES
from .base import OCDBase, LinkBase, OCDIDField, RelatedBase
from .division import Division


class Jurisdiction(OCDBase):
    id = OCDIDField(ocd_type='jurisdiction')
    name = models.CharField(max_length=300)
    url = models.URLField(max_length=2000)
    classification = models.CharField(max_length=50, choices=JURISDICTION_CLASSIFICATION_CHOICES,
                                      default='government', db_index=True)
    feature_flags = ArrayField(dbtype="text")
    division = models.ForeignKey(Division, related_name='jurisdictions', db_index=True)

    def __str__(self):
        return self.name


class LegislativeSession(RelatedBase):
    jurisdiction = models.ForeignKey(Jurisdiction, related_name='legislative_sessions')
    identifier = models.CharField(max_length=100)
    name = models.CharField(max_length=300)
    classification = models.CharField(max_length=100, choices=SESSION_CLASSIFICATION_CHOICES)
    start_date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]
    end_date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]

    def __str__(self):
        return '{} {} Session'.format(self.jurisdiction, self.name)
