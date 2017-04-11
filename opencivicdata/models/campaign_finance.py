from django.db import models
from django.contrib.postgres.fields import ArrayField

from .base import OCDBase, OCDIDField
from .jurisdiction import Jurisdiction
from .people_orgs import Organization
from .. import common


class CommitteeType(OCDBase):
    id = OCDIDField(ocd_type='campaign-finance-committee-type')
    name = models.TextField()

    jurisdiction = models.ForeignKey(Jurisdiction, related_name='campfin_committee_types')


class Committee(OCDBase):
    id = OCDIDField(ocd_type='campaign-finance-committee')
    committee_type = models.ForeignKey(CommitteeType, related_name='campfin_committees')

    statuses = ArrayField(base_field=)


class Election(OCDBase):
    # Just implementing here as stub for now
    id = OCDIDField(ocd_type='election')


class Filing(OCDBase):
    id = OCDIDField(ocd_type='campaign-finance-filing')
    identifiers = models.TextField(blank=True)
    classification = models.CharField(max_length=100)

    filer = models.ForeignKey(Committee, related_name='campfin_filings')

    coverage_start_date = models.DateTimeField(blank=True)
    coverage_end_date = models.DateTimeField(blank=True)

    recipient = models.ForeignKey(Organization, related_name='campfin_filings')

    election = ManyToManyField(Election)


class FilingSource(OCDBase):
    url = models.URLField(max_length=2000)
    note = models.TextField(blank=True)

    filing = models.ForeignKey(Filing, related_name='sources')


class FilingAction(OCDBase):
    id = OCDIDField(ocd_type='campaign-finance-filing-action')

    description = models.TextField()

    date = models.DateTimeField()

    classification =