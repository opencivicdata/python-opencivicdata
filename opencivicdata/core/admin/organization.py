from django.urls import reverse
from django.contrib import admin
from .. import models
from .base import (
    ModelAdmin,
    ReadOnlyTabularInline,
    IdentifierInline,
    LinkInline,
    ContactDetailInline,
    OtherNameInline,
)


class OrganizationIdentifierInline(IdentifierInline):
    model = models.OrganizationIdentifier


class OrganizationNameInline(OtherNameInline):
    model = models.OrganizationName


class OrganizationContactDetailInline(ContactDetailInline):
    model = models.OrganizationContactDetail


class OrganizationLinkInline(LinkInline):
    model = models.OrganizationLink


class OrganizationSourceInline(LinkInline):
    model = models.OrganizationSource


class PostInline(admin.TabularInline):
    """ a read-only inline for posts here, with links to the real thing """

    model = models.Post
    extra = 0
    fields = readonly_fields = ("label", "role")
    ordering = ("label",)
    can_delete = False
    show_change_link = True

    def has_add_permission(self, request):
        return False


class OrgMembershipInline(ReadOnlyTabularInline):
    model = models.Membership
    fk_name = "organization"
    readonly_fields = ("id", "person", "post", "label", "role", "start_date")
    fields = readonly_fields + ("end_date",)
    extra = 0
    can_delete = False


@admin.register(models.Organization)
class OrganizationAdmin(ModelAdmin):
    readonly_fields = (
        "id",
        "name",
        "classification",
        "parent",
        "jurisdiction",
        "extras",
    )
    fields = readonly_fields + (("founding_date", "dissolution_date"), "image")
    search_fields = ("name",)
    list_filter = ("jurisdiction__name",)

    inlines = [
        OrganizationIdentifierInline,
        OrganizationNameInline,
        OrganizationContactDetailInline,
        OrganizationLinkInline,
        OrganizationSourceInline,
        PostInline,
        OrgMembershipInline,
    ]

    def get_org_name(self, obj):
        parent = obj.parent
        if parent:
            return "{org} ({parent})".format(org=obj.name, parent=parent.name)
        return obj.name

    get_org_name.short_description = "Name"
    get_org_name.allow_tags = True
    get_org_name.admin_order_field = "name"

    def get_jurisdiction(self, obj):
        jurisdiction = obj.jurisdiction
        if jurisdiction:
            admin_url = reverse(
                "admin:core_jurisdiction_change", args=(jurisdiction.pk,)
            )
            tmpl = '<a href="%s">%s</a>'
            return tmpl % (admin_url, jurisdiction.name)

        return "(none)"

    get_jurisdiction.short_description = "Jurisdiction"
    get_jurisdiction.allow_tags = True
    get_jurisdiction.admin_order_field = "jurisdiction__name"

    list_select_related = ("jurisdiction",)
    list_display = ("get_org_name", "get_jurisdiction", "classification")
    ordering = ("name",)
