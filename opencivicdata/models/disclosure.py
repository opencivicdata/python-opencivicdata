from django.contrib.gis.db import models
from .base import (OCDBase, LinkBase, OCDIDField, MimetypeLinkBase,
                   RelatedEntityBase, IdentifierBase)
from .jurisdiction import Jurisdiction
from .event import Event


class Disclosure(OCDBase):
    id = OCDIDField(ocd_type='disclosure')
    name = models.CharField(max_length=300)
    jurisdiction = models.ForeignKey(Jurisdiction, related_name='disclosures')
    description = models.TextField()
    classification = models.CharField(max_length=100)
    effective_date = models.DateTimeField()
    submitted_date = models.DateTimeField()
    timezone = models.CharField(max_length=300)
    source_identified = models.NullBooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        index_together = [
            ['jurisdiction', 'classification', 'effective_date']
        ]


class DisclosureRelatedEntity(RelatedEntityBase):
    disclosure = models.ForeignKey(Disclosure, related_name="related_entities")
    note = models.TextField()
    classification = models.TextField()
    event = models.ForeignKey(Event, null=True)
    
    @property
    def entity_id(self):
        if self.entity_type == 'event':
            return self.event_id
        return super(DisclosureRelatedEntity, self).entity_id


class DisclosureDocument(LinkBase):
    disclosure = models.ForeignKey(Disclosure, related_name="documents")
    date = models.CharField(max_length=10)


class DisclosureDocumentLink(MimetypeLinkBase):
    document = models.ForeignKey(DisclosureDocument, related_name="links")


class DisclosureSource(LinkBase):
    disclosure = models.ForeignKey(Disclosure, related_name="sources")


class DisclosureIdentifier(IdentifierBase):
    disclosure = models.ForeignKey(Disclosure, related_name="identifiers")
