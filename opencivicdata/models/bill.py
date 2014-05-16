from django.db import models
from djorm_pgarray.fields import ArrayField

from .base import OCDBase, LinkBase, OCDIDField, RelatedBase
from .people_orgs import Organization, Person
from .jurisdiction import JurisdictionSession
from .. import common


class RelatedEntityBase(RelatedBase):
    name = models.CharField(max_length=300)
    entity_type = models.CharField(max_length=20)

    # optionally tied to an organization or person if it was linkable
    organization = models.ForeignKey(Organization, null=True)
    person = models.ForeignKey(Person, null=True)

    @property
    def entity_name(self):
        if entity_type == 'organization' and self.organization_id:
            return self.organization.name
        elif entity_type == 'person' and self.person_id:
            return self.person.name
        else:
            return self.name

    class Meta:
        abstract = True


class BillLinkBase(RelatedBase):
    mimetype = models.CharField(max_length=100)
    url = models.URLField()

    class Meta:
        abstract = True


# the actual models

class Bill(OCDBase):
    id = OCDIDField(ocd_type='bill')
    session = models.ForeignKey(JurisdictionSession, related_name='bills')
    name = models.CharField(max_length=100)

    title = models.TextField()

    from_organization = models.ForeignKey(Organization, related_name='bills', null=True)
    classification = ArrayField(dbtype="text")      # check that array values are in enum?
    subject = ArrayField(dbtype="text")

    def __str__(self):
        return '{} in {}'.format(self.name, self.session)


class BillSummary(RelatedBase):
    bill = models.ForeignKey(Bill, related_name='summaries')
    text = models.TextField()
    note = models.TextField(blank=True)


class BillTitle(RelatedBase):
    bill = models.ForeignKey(Bill, related_name='other_titles')
    text = models.TextField()
    note = models.TextField(blank=True)


class BillName(RelatedBase):
    bill = models.ForeignKey(Bill, related_name='other_names')
    name = models.CharField(max_length=100)
    note = models.TextField(blank=True)


class BillAction(RelatedBase):
    bill = models.ForeignKey(Bill, related_name='actions')
    actor = models.CharField(max_length=100)
    description = models.TextField()
    date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]
    classification = ArrayField(dbtype="text")      # enum
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']


class BillActionRelatedEntity(RelatedEntityBase):
    action = models.ForeignKey(BillAction, related_name='related_entities')


class RelatedBill(RelatedBase):
    bill = models.ForeignKey(Bill, related_name='related_bills')
    related_bill = models.ForeignKey(Bill, related_name='related_bills_reverse', null=True)
    name = models.CharField(max_length=100)
    session = models.CharField(max_length=100)   # should this be a FK?
    relation_type = models.CharField(max_length=100, choices=common.BILL_RELATION_TYPE_CHOICES)

    def __str__(self):
        return 'relationship of {} to {} ({})'.format(self.bill, self.related_bill,
                                                      self.relation_type)



class BillSponsor(RelatedEntityBase):
    bill = models.ForeignKey(Bill, related_name='sponsors')
    primary = models.BooleanField(default=False)
    classification = models.CharField(max_length=100)   # enum?

    def __str__(self):
        return '{} ({}) sponsorship of {}'.format(self.name, self.entity_type, self.bill)


class BillDocument(RelatedBase):
    bill = models.ForeignKey(Bill, related_name='documents')
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=100)
    date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]


class BillVersion(RelatedBase):
    bill = models.ForeignKey(Bill, related_name='versions')
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=100)
    date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]


class BillDocumentLink(BillLinkBase):
    document = models.ForeignKey(BillDocument, related_name='links')


class BillVersionLink(BillLinkBase):
    document = models.ForeignKey(BillVersion, related_name='links')


class BillSource(LinkBase):
    person = models.ForeignKey(Bill, related_name='sources')
