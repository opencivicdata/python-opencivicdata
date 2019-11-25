from django.urls import reverse
from django.contrib import admin
from django.utils.safestring import mark_safe
from .. import models
from .base import (
    ModelAdmin,
    ReadOnlyTabularInline,
    IdentifierInline,
    ContactDetailInline,
    OtherNameInline,
)


class PersonIdentifierInline(IdentifierInline):
    model = models.PersonIdentifier


class PersonNameInline(OtherNameInline):
    model = models.PersonName


class PersonContactDetailInline(ContactDetailInline):
    model = models.PersonContactDetail


class PersonLinkInline(ReadOnlyTabularInline):
    readonly_fields = ("url", "note")
    model = models.PersonLink


class PersonSourceInline(ReadOnlyTabularInline):
    readonly_fields = ("url", "note")
    model = models.PersonSource


class MembershipInline(ReadOnlyTabularInline):
    model = models.Membership
    readonly_fields = ("organization", "post", "label", "role", "start_date")
    fields = ("id",) + readonly_fields + ("end_date",)
    exclude = ("id",)
    extra = 0
    can_delete = False


# TODO field locking
@admin.register(models.Person)
class PersonAdmin(ModelAdmin):
    search_fields = ["name"]
    readonly_fields = ("id", "name", "extras")
    fields = (
        "name",
        "id",
        "image",
        ("birth_date", "death_date"),
        ("gender", "national_identity", "sort_name", "summary"),
        "biography",
        "extras",
    )
    ordering = ("name",)
    list_filter = ("memberships__organization__jurisdiction__name",)

    inlines = [
        PersonIdentifierInline,
        PersonNameInline,
        PersonContactDetailInline,
        PersonLinkInline,
        PersonSourceInline,
        MembershipInline,
    ]

    def get_memberships(self, obj):
        memberships = obj.memberships.select_related("organization__jurisdiction")
        html = []
        SHOW_N = 5
        for memb in memberships[:SHOW_N]:
            org = memb.organization
            admin_url = reverse("admin:core_organization_change", args=(org.pk,))
            tmpl = '<a href="%s">%s%s</a>\n'
            html.append(
                tmpl
                % (
                    admin_url,
                    (
                        memb.organization.jurisdiction.name + ": "
                        if memb.organization.jurisdiction
                        else ""
                    ),
                    memb.organization.name,
                )
            )
        more = len(memberships) - SHOW_N
        if 0 < more:
            html.append("And %d more" % more)
        return mark_safe("<br/>".join(html))

    get_memberships.short_description = "Memberships"

    list_display = ("name", "id", "get_memberships")
