from django.db import models
from djorm_pgarray.fields import ArrayField

from ..common import JURISDICTION_CLASSIFICATION_CHOICES, SESSION_CLASSIFICATION_CHOICES
from .base import OCDBase, LinkBase, OCDIDField, RelatedBase
from .division import Division


class Jurisdiction(OCDBase):
    id = OCDIDField(ocd_type='jurisdiction')
    name = models.CharField(max_length=300)
    url = models.URLField()
    classification = models.CharField(max_length=50, choices=JURISDICTION_CLASSIFICATION_CHOICES,
                                      default='government')
    feature_flags = ArrayField(dbtype="text")
    division = models.ForeignKey(Division, related_name='jurisdictions')


class JurisdictionSession(RelatedBase):
    jurisdiction = models.ForeignKey(Jurisdiction, related_name='sessions')
    name = models.CharField(max_length=300)
    classification = models.CharField(max_length=100, choices=SESSION_CLASSIFICATION_CHOICES)
    start_date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]
    end_date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]
