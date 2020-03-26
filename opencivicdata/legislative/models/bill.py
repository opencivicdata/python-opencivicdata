from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex


from opencivicdata.core.models.base import (
    OCDBase,
    LinkBase,
    OCDIDField,
    RelatedBase,
    RelatedEntityBase,
    MimetypeLinkBase,
    IdentifierBase,
)
from opencivicdata.core.models import Organization
from .session import LegislativeSession
from ... import common


class Bill(OCDBase):
    id = OCDIDField(ocd_type="bill")
    legislative_session = models.ForeignKey(
        LegislativeSession,
        related_name="bills",
        # sessions should be hard to delete
        on_delete=models.PROTECT,
    )
    identifier = models.CharField(max_length=100)

    title = models.TextField()

    from_organization = models.ForeignKey(
        Organization,
        related_name="bills",
        null=True,
        # chambers should be hard to delete
        on_delete=models.PROTECT,
    )
    # check that array values are in enum?
    classification = ArrayField(base_field=models.TextField(), blank=True, default=list)
    subject = ArrayField(base_field=models.TextField(), blank=True, default=list)

    def __str__(self):
        return "{} in {}".format(self.identifier, self.legislative_session)

    class Meta:
        db_table = "opencivicdata_bill"
        index_together = [["from_organization", "legislative_session", "identifier"]]


class BillAbstract(RelatedBase):
    bill = models.ForeignKey(Bill, related_name="abstracts", on_delete=models.CASCADE)
    abstract = models.TextField()
    note = models.TextField(blank=True)
    date = models.TextField(max_length=10, blank=True)  # YYYY[-MM[-DD]]

    def __str__(self):
        return "{0} abstract".format(self.bill.identifier)

    class Meta:
        db_table = "opencivicdata_billabstract"


class BillTitle(RelatedBase):
    bill = models.ForeignKey(
        Bill, related_name="other_titles", on_delete=models.CASCADE
    )
    title = models.TextField()
    note = models.TextField(blank=True)

    def __str__(self):
        return "{0} ({1})".format(self.title, self.bill.identifier)

    class Meta:
        db_table = "opencivicdata_billtitle"


class BillIdentifier(IdentifierBase):
    bill = models.ForeignKey(
        Bill, related_name="other_identifiers", on_delete=models.CASCADE
    )
    note = models.TextField(blank=True)

    class Meta:
        db_table = "opencivicdata_billidentifier"


class BillAction(RelatedBase):
    bill = models.ForeignKey(Bill, related_name="actions", on_delete=models.CASCADE)
    organization = models.ForeignKey(
        Organization,
        related_name="actions",
        # don't let an org delete wipe out a bunch of bill actions
        on_delete=models.PROTECT,
    )
    description = models.TextField()
    date = models.CharField(max_length=25)  # YYYY-MM-DD HH:MM:SS+HH:MM
    classification = ArrayField(
        base_field=models.TextField(), blank=True, default=list
    )  # enum
    order = models.PositiveIntegerField()
    extras = JSONField(default=dict, blank=True)

    class Meta:
        db_table = "opencivicdata_billaction"
        ordering = ["order"]

    def __str__(self):
        return "{0} action on {1}".format(self.bill.identifier, self.date)


class BillActionRelatedEntity(RelatedEntityBase):
    action = models.ForeignKey(
        BillAction, related_name="related_entities", on_delete=models.CASCADE
    )

    def __str__(self):
        return "{0} related to {1}".format(self.entity_name, self.action)

    class Meta:
        db_table = "opencivicdata_billactionrelatedentity"


class RelatedBill(RelatedBase):
    bill = models.ForeignKey(
        Bill, related_name="related_bills", on_delete=models.CASCADE
    )
    related_bill = models.ForeignKey(
        Bill,
        related_name="related_bills_reverse",
        null=True,
        # if related bill goes away, just unlink the relationship
        on_delete=models.SET_NULL,
    )
    identifier = models.CharField(max_length=100)
    # not a FK in case we don't know the session yet
    legislative_session = models.CharField(max_length=100)
    relation_type = models.CharField(
        max_length=100, choices=common.BILL_RELATION_TYPE_CHOICES
    )

    def __str__(self):
        return "relationship of {} to {} ({})".format(
            self.bill, self.related_bill, self.relation_type
        )

    class Meta:
        db_table = "opencivicdata_relatedbill"


class BillSponsorship(RelatedEntityBase):
    bill = models.ForeignKey(
        Bill, related_name="sponsorships", on_delete=models.CASCADE
    )
    primary = models.BooleanField(default=False)
    classification = models.CharField(max_length=100)  # enum?

    def __str__(self):
        return "{} ({}) sponsorship of {}".format(
            self.name, self.entity_type, self.bill
        )

    class Meta:
        db_table = "opencivicdata_billsponsorship"


class BillDocument(RelatedBase):
    bill = models.ForeignKey(Bill, related_name="documents", on_delete=models.CASCADE)
    note = models.CharField(max_length=300)
    date = models.CharField(max_length=10)  # YYYY[-MM[-DD]]
    extras = JSONField(default=dict, blank=True)

    def __str__(self):
        return "{0} document of {1}".format(self.date, self.bill)

    class Meta:
        db_table = "opencivicdata_billdocument"


class BillVersion(RelatedBase):
    bill = models.ForeignKey(Bill, related_name="versions", on_delete=models.CASCADE)
    note = models.CharField(max_length=300)
    date = models.CharField(max_length=10)  # YYYY[-MM[-DD]]
    extras = JSONField(default=dict, blank=True)

    def __str__(self):
        return "{0} version of {1}".format(self.date, self.bill)

    class Meta:
        db_table = "opencivicdata_billversion"


class BillDocumentLink(MimetypeLinkBase):
    document = models.ForeignKey(
        BillDocument, related_name="links", on_delete=models.CASCADE
    )

    def __str__(self):
        return "{0} for {1}".format(self.url, self.document.bill)

    class Meta:
        db_table = "opencivicdata_billdocumentlink"


class BillVersionLink(MimetypeLinkBase):
    version = models.ForeignKey(
        BillVersion, related_name="links", on_delete=models.CASCADE
    )

    def __str__(self):
        return "{0} for {1}".format(self.url, self.version)

    class Meta:
        db_table = "opencivicdata_billversionlink"


class BillSource(LinkBase):
    bill = models.ForeignKey(Bill, related_name="sources", on_delete=models.CASCADE)

    class Meta:
        db_table = "opencivicdata_billsource"


class SearchableBill(models.Model):
    """
    This model associates a single version's text with a given bill.

    This is done for a few reasons:
        * bills with multiple versions aren't weighted more heavily than others
        * this makes querying quite a bit more efficient (no need to deduplicate results)

    We'll also store error results, assuming that they're somewhat persistent.
    """

    bill = models.OneToOneField(
        Bill, related_name="searchable", null=True, on_delete=models.CASCADE
    )
    version_link = models.OneToOneField(
        BillVersionLink, related_name="searchable", null=True, on_delete=models.CASCADE
    )

    search_vector = SearchVectorField(default=None)
    all_titles = models.TextField(default="")
    raw_text = models.TextField(default="")
    is_error = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "opencivicdata_searchablebill"
        indexes = [GinIndex(name="search_index", fields=["search_vector"])]
