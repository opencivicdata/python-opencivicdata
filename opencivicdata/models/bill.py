from django.db import models

from .base import OCDIDField, RelatedEntityBase, RelatedBase, MimetypeLinkBase, LinkBase
from .jurisdiction import LegislativeSession
from .people_orgs import Organization
from .document import (Document, DocumentAbstract, DocumentIdentifier,
                       DocumentAction, DocumentTitle, RelatedDocument,
                       DocumentVersion)
from .. import common

class Bill(Document) :
    id = OCDIDField(ocd_type='bill')
    from_organization = models.ForeignKey(Organization, 
                                          related_name='bills',
                                          null=True)
    legislative_session = models.ForeignKey(LegislativeSession, 
                                            related_name='bills')

    def __str__(self):
        return '{} in {}'.format(self.identifier, self.legislative_session)

    class Meta:
        index_together = [
            ['from_organization', 'legislative_session', 'identifier'],
        ]

class BillAbstract(DocumentAbstract):
    bill = models.ForeignKey(Bill, related_name='abstracts')

class BillTitle(DocumentTitle):
    bill = models.ForeignKey(Bill, related_name='other_titles')

class BillIdentifier(DocumentIdentifier):
    bill = models.ForeignKey(Bill, related_name='other_identifiers')

class BillAction(DocumentAction):
    bill = models.ForeignKey(Bill, related_name='actions')
    organization = models.ForeignKey(Organization, related_name='bill_actions')

class BillActionRelatedEntity(RelatedEntityBase):
    action = models.ForeignKey(BillAction, related_name='related_entities')

class RelatedBill(RelatedDocument):
    bill = models.ForeignKey(Bill, related_name='related_bills')
    related_bill = models.ForeignKey(Bill, related_name='related_bills_reverse', null=True)
    # not a FK in case we don't know the session yet
    legislative_session = models.CharField(max_length=100)
    relation_type = models.CharField(max_length=100, choices=common.BILL_RELATION_TYPE_CHOICES)

    def __str__(self):
        return 'relationship of {} to {} ({})'.format(self.bill, self.related_bill,
                                                      self.relation_type)

class BillSponsorship(RelatedEntityBase):
    bill = models.ForeignKey(Bill, related_name='sponsorships')
    primary = models.BooleanField(default=False)
    classification = models.CharField(max_length=100)   # enum?

    def __str__(self):
        return '{} ({}) sponsorship of {}'.format(self.name, self.entity_type, self.bill)

class BillDocument(RelatedBase):
    bill = models.ForeignKey(Bill, related_name='documents')
    note = models.CharField(max_length=300)
    date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]

class BillVersion(DocumentVersion):
    bill = models.ForeignKey(Bill, related_name='versions')

class BillDocumentLink(MimetypeLinkBase):
    document = models.ForeignKey(BillDocument, related_name='links')

class BillVersionLink(MimetypeLinkBase):
    version = models.ForeignKey(BillVersion, related_name='links')


class BillSource(LinkBase):
    bill = models.ForeignKey(Bill, related_name='sources')
