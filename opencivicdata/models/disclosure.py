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

    def __str__(self):
        return self.name

    class Meta:
        index_together = [
            ['jurisdiction', 'classification', 'effective_date']
        ]


class DisclosureRegistrant(RelatedEntityBase):

    disclosure = models.ForeignKey(Disclosure, related_name="registrant")

    def __str__(self):
        tmpl = '{reg}: {dc} ({dd})'
        return tmpl.format(reg=self.name,
                           dc=self.disclosure.classification,
                           dd=self.disclosure.submitted_date)


class DisclosureAuthority(RelatedEntityBase):

    disclosure = models.ForeignKey(Disclosure, related_name="authority")

    def __str__(self):
        tmpl = '{reg}: {dc} ({dd})'
        return tmpl.format(reg=self.name,
                           dc=self.disclosure.classification,
                           dd=self.disclosure.submitted_date)


class DisclosureRelatedEntity(RelatedEntityBase):
    disclosure = models.ForeignKey(Disclosure, related_name="related_entities")
    note = models.TextField()


class DisclosureDisclosedEvent(RelatedEntityBase):
    event = models.ForeignKey(Event)
    disclosure = models.ForeignKey(Disclosure, related_name="disclosed_events")


class DisclosureDocument(LinkBase):
    disclosure = models.ForeignKey(Disclosure, related_name="documents")
    date = models.CharField(max_length=10)


class DisclosureDocumentLink(MimetypeLinkBase):
    document = models.ForeignKey(DisclosureDocument, related_name="links")


class DisclosureSource(LinkBase):
    disclosure = models.ForeignKey(Disclosure, related_name="sources")


class DisclosureIdentifier(IdentifierBase):
    disclosure = models.ForeignKey(Disclosure, related_name="identifiers")
