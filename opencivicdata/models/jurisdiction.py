from django.db import models
from djorm_pgarray.fields import ArrayField

from .base import OCDBase, LinkBase, OCDIDField, RelatedBase
from .division import Division


class Jurisdiction(OCDBase):
    id = OCDIDField(ocd_type='jurisdiction')
    name = models.CharField(max_length=300)
    url = models.URLField()
    feature_flags = ArrayField(dbtype="text")
    division = models.ForeignKey(Division, related_name='jurisdictions')


class JurisdictionSession(RelatedBase):
    jurisdiction = models.ForeignKey(Jurisdiction, related_name='sessions')
    name = models.CharField(max_length=300)
    classification = models.CharField(max_length=100)     # enum?
    start_date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]
    end_date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]


class JurisdictionBuildingMap(LinkBase):
    jurisdiction = models.ForeignKey(Jurisdiction, related_name='building_maps')
    order = models.PositiveIntegerField()
