from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.encoding import python_2_unicode_compatible

from ...common import JURISDICTION_CLASSIFICATION_CHOICES
from .base import OCDBase, OCDIDField
from .division import Division


@python_2_unicode_compatible
class Jurisdiction(OCDBase):
    id = OCDIDField(ocd_type='jurisdiction')
    name = models.CharField(max_length=300)
    url = models.URLField(max_length=2000)
    classification = models.CharField(max_length=50, choices=JURISDICTION_CLASSIFICATION_CHOICES,
                                      default='government', db_index=True)
    feature_flags = ArrayField(base_field=models.TextField(), blank=True, default=list)
    division = models.ForeignKey(Division, related_name='jurisdictions', db_index=True)

    class Meta:
        db_table = 'opencivicdata_jurisdiction'

    def __str__(self):
        return self.name
