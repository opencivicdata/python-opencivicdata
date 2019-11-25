from django.contrib import admin
from django.template import defaultfilters
from opencivicdata.core.admin.base import (
    ModelAdmin,
    ReadOnlyTabularInline,
    IdentifierInline,
)
from .. import models


class BillAbstractInline(ReadOnlyTabularInline):
    model = models.BillAbstract
    readonly_fields = ("abstract", "note")
    can_delete = False


class BillTitleInline(ReadOnlyTabularInline):
    model = models.BillTitle
    readonly_fields = ("title", "note")
    can_delete = False


class BillIdentifierInline(IdentifierInline):
    model = models.BillIdentifier


class BillActionInline(ReadOnlyTabularInline):
    model = models.BillAction

    def get_related_entities(self, obj):
        ents = obj.related_entities.all()
        ent_list = [e.name for e in ents]
        return ", ".join(ent_list)

    get_related_entities.short_description = "Related Entities"
    get_related_entities.allow_tags = True

    list_select_related = ("BillActionRelatedEntity",)
    readonly_fields = ("date", "organization", "description", "get_related_entities")


class RelatedBillInline(ReadOnlyTabularInline):
    model = models.RelatedBill
    fk_name = "bill"
    readonly_fields = fields = ("identifier", "legislative_session", "relation_type")
    extra = 0


class BillSponsorshipInline(ReadOnlyTabularInline):
    model = models.BillSponsorship
    readonly_fields = fields = ("name", "primary", "classification")
    extra = 0


class DocVersionInline(ReadOnlyTabularInline):
    model = models.BillVersion

    def get_links(self, obj):
        return "<br />".join(
            '<a href="{0}">{0}</a>'.format(link.url) for link in obj.links.all()
        )

    get_links.short_description = "Links"
    get_links.allow_tags = True

    list_select_related = ("BillVersionLink",)
    readonly_fields = ("note", "date", "get_links")


class BillVersionInline(DocVersionInline):
    model = models.BillVersion


class BillDocumentInline(DocVersionInline):
    model = models.BillDocument


class BillSourceInline(ReadOnlyTabularInline):
    readonly_fields = ("url", "note")
    model = models.BillSource


@admin.register(models.Bill)
class BillAdmin(ModelAdmin):
    readonly_fields = fields = (
        "identifier",
        "legislative_session",
        "bill_classifications",
        "from_organization",
        "title",
        "id",
        "subject",
        "extras",
    )
    search_fields = ["identifier", "title"]
    list_select_related = ("legislative_session", "legislative_session__jurisdiction")
    inlines = [
        BillAbstractInline,
        BillTitleInline,
        BillIdentifierInline,
        BillActionInline,
        BillSponsorshipInline,
        BillSourceInline,
        RelatedBillInline,
        BillVersionInline,
        BillDocumentInline,
    ]

    def bill_classifications(self, obj):
        return ", ".join(obj.classification)

    def get_jurisdiction_name(self, obj):
        return obj.legislative_session.jurisdiction.name

    get_jurisdiction_name.short_description = "Jurisdiction"

    def get_session_name(self, obj):
        return obj.legislative_session.name

    get_session_name.short_description = "Session"
    get_session_name.admin_order_field = "legislative_session__name"

    def get_truncated_sponsors(self, obj):
        spons = ", ".join(s.name for s in obj.sponsorships.all()[:5])
        return defaultfilters.truncatewords(spons, 10)

    get_truncated_sponsors.short_description = "Sponsors"

    def get_truncated_title(self, obj):
        return defaultfilters.truncatewords(obj.title, 25)

    get_truncated_title.short_description = "Title"

    list_display = (
        "identifier",
        "get_jurisdiction_name",
        "get_session_name",
        "get_truncated_sponsors",
        "get_truncated_title",
    )

    list_filter = ("legislative_session__jurisdiction__name",)
