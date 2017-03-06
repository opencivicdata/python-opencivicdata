from django.db import models

from .base import OCDIDField, RelatedEntityBase, OCDBase
from .document import Document, RelatedDocument
from .people_orgs import Organization
from .. import common

class Filing(Document, OCDBase) :
    id = OCDIDField(ocd_type='filing')
    from_organization = models.ForeignKey(Organization, 
                                          related_name='filings',
                                          null=True)

    def __str__(self):
        return '{}'.format(self.identifier)

    class Meta:
        index_together = [
            ['from_organization', 'identifier'],
        ]


class FilingAuthorship(RelatedEntityBase):
    document = models.ForeignKey(Filing, related_name='authorship')
    classification = models.CharField(max_length=100)   # enum?
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']


    def __str__(self):
        return '{} ({}) authorship of {}'.format(self.name, self.entity_type, self.document)


class RelatedFiling(RelatedDocument):
    relation_type = models.CharField(max_length=100, choices=common.FILING_RELATION_TYPE_CHOICES)
