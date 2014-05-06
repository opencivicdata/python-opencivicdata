from django.db import models
from djorm_pgarray.fields import ArrayField

from .base import CommonBase, LinkBase
from .people_orgs import Organization, Person
from .jurisdiction import JurisdictionSession


class Bill(CommonBase):
    id = models.CharField(max_length=100, primary_key=True)
    session = models.ForeignKey(JurisdictionSession, related_name='bills')
    name = models.CharField(max_length=100)

    title = models.TextField()

    organization = models.ForeignKey(Organization, related_name='bills')
    classification = ArrayField(dbtype="text")
    subjects = ArrayField(dbtype="text")


class BillSummary(models.Model):
    bill = models.ForeignKey(Bill, related_name='summaries')
    text = models.TextField()
    note = models.TextField(blank=True)


class BillTitle(models.Model):
    bill = models.ForeignKey(Bill, related_name='other_titles')
    text = models.TextField()
    note = models.TextField(blank=True)


class BillName(models.Model):
    bill = models.ForeignKey(Bill, related_name='other_names')
    name = models.CharField(max_length=100)
    note = models.TextField(blank=True)


class RelatedBill(models.Model):
    bill = models.ForeignKey(Bill, related_name='related_bills')
    related_bill = models.ForeignKey(Bill, related_name='related_bills_reverse')
    relation_type = models.CharField(max_length=100)        # enum?


class BillSponsor(models.Model):
    bill = models.ForeignKey(Bill, related_name='sponsors')
    name = models.CharField(max_length=300)
    primary = models.BooleanField(default=False)
    classification = models.CharField(max_length=100)   # enumeration?

    # optionally tied to an organization or person if it was linkable
    # TODO: find way to enforce that only one of these is true?
    organization = models.ForeignKey(Organization, related_name='sponsorships', null=True)
    person = models.ForeignKey(Person, related_name='sponsorships', null=True)


class BillDocument(models.Model):
    bill = models.ForeignKey(Bill, related_name='documents')
    name = models.CharField(max_length=300)
    classification = models.CharField(max_length=100)   # enum?
    date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]


class BillVersion(models.Model):
    bill = models.ForeignKey(Bill, related_name='versions')
    name = models.CharField(max_length=300)
    classification = models.CharField(max_length=100)   # enum?
    date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]


class BillLink(models.Model):
    mimetype = models.CharField(max_length=100)
    url = models.URLField()

    class Meta:
        abstract = True


class BillDocumentLink(BillLink):
    document = models.ForeignKey(BillDocument, related_name='links')


class BillVersionLink(BillLink):
    document = models.ForeignKey(BillVersion, related_name='links')


class BillSource(LinkBase):
    person = models.ForeignKey(Bill, related_name='sources')
