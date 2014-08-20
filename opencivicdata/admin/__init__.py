from django.contrib import admin
from django.core import urlresolvers
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

### People & Memberships #######

class PersonIdentifierInline(IdentifierInline):
    model = models.PersonIdentifier


class PersonNameInline(OtherNameInline):
    model = models.PersonName


class PersonContactDetailInline(ContactDetailInline):
    model = models.PersonContactDetail


class PersonLinkInline(LinkInline):
    model = models.PersonLink


class PersonSourceInline(LinkInline):
    model = models.PersonSource


class MembershipInline(NoAddTabularInline):
    model = models.Membership
    readonly_fields = ('organization', 'post')
    fields = ('organization', 'post', 'label', 'role', 'start_date', 'end_date')
    extra = 0
    can_delete = False


@admin.register(models.Person)
class PersonAdmin(ModelAdmin):
    search_fields = ['name']
    readonly_fields = ('id', 'name', 'extras')
    fields = (
        'name', 'id', 'image',
        ('birth_date', 'death_date'),
        ('gender', 'national_identity', 'sort_name', 'summary'),
        'biography', 'extras',
    )

    inlines = [
        PersonIdentifierInline,
        PersonNameInline,
        PersonContactDetailInline,
        PersonLinkInline,
        PersonSourceInline,
        MembershipInline
    ]


    def get_memberships(self, obj):
        memberships = obj.memberships.select_related('organization__jurisdiction')
        html = []
        SHOW_N = 5
        for memb in memberships[:SHOW_N]:
            info = (memb._meta.app_label, memb._meta.module_name)
            admin_url = ''#urlresolvers.reverse('admin:%s_%s_change' % info, args=(memb.pk,))
            tmpl = '<a href="%s">%s %s</a>\n'
            html.append(tmpl % (
                admin_url,
                memb.organization.jurisdiction.name,
                memb.organization.name))
        more = len(memberships) - SHOW_N
        if 0 < more:
            html.append('And %d more' % more)
        return '<br/>'.join(html)

    get_memberships.short_description = 'Memberships'
    get_memberships.allow_tags = True

    list_selected_related = ('memberships',)
    list_display = ('name', 'id', 'get_memberships')


class MembershipContactDetailInline(ContactDetailInline):
    model = models.MembershipContactDetail


class MembershipLinkInline(LinkInline):
    model = models.MembershipLink


@admin.register(models.Membership)
class MembershipAdmin(ModelAdmin):
    readonly_fields = ('organization', 'person', 'post', 'on_behalf_of', 'extras')
    list_display = ('organization', 'person', 'post', 'on_behalf_of',
                    'label', 'role', 'start_date', 'end_date',)
    fields = ('organization', 'person', 'role', 'post', 'label', 'on_behalf_of',
              ('start_date', 'end_date'), 'extras')
    inlines = [
        MembershipContactDetailInline,
        MembershipLinkInline,
    ]
