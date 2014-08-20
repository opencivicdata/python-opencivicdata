from django.contrib import admin
from .. import models

# Helpers ##########

class ModelAdmin(admin.ModelAdmin):
    """ deletion of top level objects is evil """
    def has_delete_permission(self, request, obj=None):
        return False


class NoAddTabularInline(admin.TabularInline):
    def has_add_permission(self, request):
        return False


class IdentifierInline(admin.TabularInline):
    fields = ('identifier', 'scheme')
    extra = 0


class LinkInline(admin.TabularInline):
    fields = ('url', 'note')
    extra = 0


class ContactDetailInline(admin.TabularInline):
    fields = ('type', 'value', 'note', 'label')
    extra = 0


class OtherNameInline(admin.TabularInline):
    fields = ('name', 'note', 'start_date', 'end_date')
    extra = 0

#class MimetypeLinkInline(admin.TabularInline):
#    fields = ('media_type', 'url')
#class RelatedEntityInline(admin.TabularInline):
#    fields = ('name', 'entity_type', 'organization', 'person')

# Divisions & Jurisdictions ##########

@admin.register(models.Division)
class DivisionAdmin(ModelAdmin):
    list_display = ('name', 'id')
    search_fields = list_display
    fields = readonly_fields = ('id', 'name', 'redirect', 'country')

class LegislativeSessionInline(NoAddTabularInline):
    model = models.LegislativeSession
    readonly_fields = ('identifier', 'name', 'classification')
    can_delete = False


@admin.register(models.Jurisdiction)
class JurisdictionAdmin(ModelAdmin):
    list_display = ('name', 'id')
    readonly_fields = fields = ('id', 'name', 'classification', 'url', 'division', 'feature_flags',
                                'extras')
    inlines = [LegislativeSessionInline]

# Organizations and Posts #############


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
    fields = readonly_fields = ('label', 'role')
    ordering = ('label',)
    can_delete = False
    show_change_link = True # Django 1.8?


@admin.register(models.Organization)
class OrganizationAdmin(ModelAdmin):
    readonly_fields = ('id', 'classification', 'parent', 'jurisdiction', 'extras')
    fields = (
        'name', 'jurisdiction', 'id', 'classification',
        'parent', ('founding_date', 'dissolution_date'),
        'image', 'extras')
    list_display = ('name', 'jurisdiction', 'classification')
    inlines = [
        OrganizationIdentifierInline,
        OrganizationNameInline,
        OrganizationContactDetailInline,
        OrganizationLinkInline,
        OrganizationSourceInline,
        PostInline
    ]

# Posts

class PostContactDetailInline(ContactDetailInline):
    model = models.PostContactDetail


class PostLinkInline(LinkInline):
    model = models.PostLink


@admin.register(models.Post)
class PostAdmin(ModelAdmin):
    readonly_fields = ('id', 'label', 'organization', 'division', 'extras', 'role')
    fields = readonly_fields + (('start_date', 'end_date'), )
    list_display = ('label', 'organization')
    inlines = [
        PostContactDetailInline,
        PostLinkInline,
    ]

