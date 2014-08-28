from django.core import urlresolvers
from django.contrib import admin
from django.template import defaultfilters
from .. import models

# Helpers ##########

class ModelAdmin(admin.ModelAdmin):
    """ deletion of top level objects is evil """
    def has_delete_permission(self, request, obj=None):
        return False


class ReadOnlyTabularInline(admin.TabularInline):
    def has_add_permission(self, request):
        return False
    can_delete = False


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

class LegislativeSessionInline(ReadOnlyTabularInline):
    model = models.LegislativeSession
    readonly_fields = ('identifier', 'name', 'classification')


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


class MembershipInline(ReadOnlyTabularInline):
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
                memb.organization.jurisdiction.name if memb.organization.jurisdiction else '',
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


# Bills ################


class BillAbstractInline(ReadOnlyTabularInline):
    model = models.BillAbstract
    readonly_fields = ('abstract', 'note')
    can_delete = False


class BillTitleInline(ReadOnlyTabularInline):
    model = models.BillTitle
    readonly_fields = ('title', 'note')
    can_delete = False


class BillIdentifierInline(IdentifierInline):
    model = models.BillIdentifier


class BillActionInline(ReadOnlyTabularInline):
    model = models.BillAction
    readonly_fields = ('date', 'organization', 'description')
    fields = ('date', 'description', 'organization')
    ordering = ('date',)

# TODO: BillActionRelatedEntity
# TODO: RelatedBill

class BillSponsorshipInline(ReadOnlyTabularInline):
    model = models.BillSponsorship
    readonly_fields = fields = ('name', 'primary', 'classification')
    extra = 0

# TODO: Document & Version

class BillSourceInline(ReadOnlyTabularInline):
    readonly_fields = ('url', 'note')
    model = models.BillSource


@admin.register(models.Bill)
class BillAdmin(admin.ModelAdmin):
    readonly_fields = fields = (
        'identifier', 'legislative_session', 'classification',
        'from_organization', 'title', 'id', 'extras')
    search_fields = ['identifier', 'title',]
    list_selected_related = (
        'sources',
        'legislative_session',
        'legislative_session__jurisdiction')
    inlines = [
        BillAbstractInline,
        BillTitleInline,
        BillIdentifierInline,
        BillActionInline,
        BillSponsorshipInline,
        BillSourceInline,
    ]

    def get_jurisdiction_name(self, obj):
        return obj.legislative_session.jurisdiction.name
    get_jurisdiction_name.short_description = 'Jurisdiction'

    def get_session_name(self, obj):
        return obj.legislative_session.name
    get_session_name.short_description = 'Session'

    def source_link(self, obj):
        source = obj.sources.filter(url__icontains="legislationdetail").get()
        tmpl = u'<a href="{0}" target="_blank">View source</a>'
        return tmpl.format(source.url)
    source_link.short_description = 'View source'
    source_link.allow_tags = True

    def get_truncated_sponsors(self, obj):
        spons = ', '.join(s.name for s in obj.sponsorships.all()[:5])
        return defaultfilters.truncatewords(spons, 10)
    get_truncated_sponsors.short_description = 'Sponsors'

    def get_truncated_title(self, obj):
        return defaultfilters.truncatewords(obj.title, 25)
    get_truncated_title.short_description = 'Title'

    list_display = (
        'identifier', 'get_jurisdiction_name',
        'get_session_name', 'get_truncated_sponsors',
        'get_truncated_title', 'source_link')

    list_filter = ('legislative_session__jurisdiction__name',)
