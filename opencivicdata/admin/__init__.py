from django.core import urlresolvers
from django.contrib import admin
from django.template import defaultfilters
from .. import models
from .base import (ModelAdmin, ReadOnlyTabularInline, IdentifierInline, LinkInline,
                   ContactDetailInline, OtherNameInline)
from . import vote


# Divisions & Jurisdictions ##########


@admin.register(models.Division)
class DivisionAdmin(ModelAdmin):
    list_display = ('name', 'id')
    search_fields = list_display
    fields = readonly_fields = ('id', 'name', 'redirect', 'country')
    ordering = ('id',)


class LegislativeSessionInline(ReadOnlyTabularInline):
    model = models.LegislativeSession
    readonly_fields = ('identifier', 'name', 'classification', 'start_date', 'end_date')
    ordering = ('-identifier',)


@admin.register(models.Jurisdiction)
class JurisdictionAdmin(ModelAdmin):
    list_display = ('name', 'id')
    readonly_fields = fields = ('id', 'name', 'division', 'classification',
                                'feature_flags', 'extras')
    fields = readonly_fields + ('url', )
    ordering = ('id',)
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
    show_change_link = True

    def has_add_permission(self, request):
        return False


class OrgMembershipInline(ReadOnlyTabularInline):
    model = models.Membership
    fk_name = "organization"
    readonly_fields = ('person', 'post')
    fields = ('person', 'post', 'label', 'role', 'start_date', 'end_date', 'id')
    extra = 0
    can_delete = True


@admin.register(models.Organization)
class OrganizationAdmin(ModelAdmin):
    readonly_fields = ('id', 'classification', 'parent', 'jurisdiction', 'extras')
    fields = (
        'name', 'jurisdiction', 'id', 'classification',
        'parent', ('founding_date', 'dissolution_date'),
        'image', 'extras')
    search_fields = ('name',)

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
            admin_url = urlresolvers.reverse('admin:opencivicdata_jurisdiction_change',
                                             args=(jurisdiction.pk,))
            tmpl = '<a href="%s">%s</a>'
            return tmpl % (admin_url, jurisdiction.name)

        return "(none)"

    get_jurisdiction.short_description = 'Jurisdiction'
    get_jurisdiction.allow_tags = True
    get_jurisdiction.admin_order_field = 'jurisdiction__name'

    list_select_related = ('jurisdiction',)
    list_display = ('get_org_name', 'get_jurisdiction', 'classification')
    ordering = ('name',)


class PostContactDetailInline(ContactDetailInline):
    model = models.PostContactDetail


class PostLinkInline(LinkInline):
    model = models.PostLink


@admin.register(models.Post)
class PostAdmin(ModelAdmin):
    readonly_fields = ('id', 'label', 'organization', 'division', 'extras', 'role')
    fields = readonly_fields + (('start_date', 'end_date'), )
    list_display = ('label', 'organization', 'division')
    ordering = ('organization__name',)
    inlines = [
        PostContactDetailInline,
        PostLinkInline,
    ]
    search_fields = ('organization__name', 'label')

# People & Memberships #######


class PersonIdentifierInline(IdentifierInline):
    model = models.PersonIdentifier


class PersonNameInline(OtherNameInline):
    model = models.PersonName


class PersonContactDetailInline(ContactDetailInline):
    model = models.PersonContactDetail


class PersonLinkInline(LinkInline):
    verbose_name = "Related link"
    verbose_name_plural = "Related links"
    model = models.PersonLink


class PersonSourceInline(LinkInline):
    verbose_name = "Source link"
    verbose_name_plural = "Source links"
    model = models.PersonSource


class MembershipInline(ReadOnlyTabularInline):
    model = models.Membership
    readonly_fields = ('organization', 'post')
    fields = ('organization', 'post', 'label', 'role', 'start_date', 'end_date', 'id')
    extra = 0
    can_delete = True


# TODO field locking
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
    ordering = ('name',)

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
            org = memb.organization
            admin_url = urlresolvers.reverse('admin:opencivicdata_organization_change',
                                             args=(org.pk,))
            tmpl = '<a href="%s">%s%s</a>\n'
            html.append(tmpl % (
                admin_url,
                (memb.organization.jurisdiction.name +
                 ": " if memb.organization.jurisdiction else ''),
                memb.organization.name))
        more = len(memberships) - SHOW_N
        if 0 < more:
            html.append('And %d more' % more)
        return '<br/>'.join(html)

    get_memberships.short_description = 'Memberships'
    get_memberships.allow_tags = True

    #list_select_related = ('memberships',)
    list_display = ('name', 'id', 'get_memberships')

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

    def get_related_entities(self, obj):
        ents = obj.related_entities.all()
        # this seems to be a uuid problem, get
        # rid of the below return stmt when uuids are fixed
        return None
        ent_list = [e.name for e in ents]
        return ', '.join(ent_list)

    get_related_entities.short_description = 'Related Entities'
    get_related_entities.allow_tags = True

    list_select_related = ('BillActionRelatedEntity',)
    readonly_fields = ('date', 'organization', 'description', 'get_related_entities')


class RelatedBillInline(ReadOnlyTabularInline):
    model = models.RelatedBill
    fk_name = 'bill'
    readonly_fields = fields = ('identifier', 'legislative_session', 'relation_type')
    extra = 0


class BillSponsorshipInline(ReadOnlyTabularInline):
    model = models.BillSponsorship
    readonly_fields = fields = ('name', 'primary', 'classification')
    extra = 0


class DocVersionInline(ReadOnlyTabularInline):
    model = models.BillVersion

    def get_links(self, obj):
        return '<br />'.join('<a href="{0}">{0}</a>'.format(link.url) for link in obj.links.all())

    get_links.short_description = 'Links'
    get_links.allow_tags = True

    list_select_related = ('BillVersionLink',)
    readonly_fields = ('note', 'date', 'get_links')


class BillVersionInline(DocVersionInline):
    model = models.BillVersion


class BillDocumentInline(DocVersionInline):
    model = models.BillDocument


class BillSourceInline(ReadOnlyTabularInline):
    readonly_fields = ('url', 'note')
    model = models.BillSource


@admin.register(models.Bill)
class BillAdmin(ModelAdmin):
    readonly_fields = fields = (
        'identifier', 'legislative_session', 'bill_classifications',
        'from_organization', 'title', 'id', 'subject', 'extras')
    search_fields = ['identifier', 'title']
    list_select_related = (
        #'sources',
        'legislative_session',
        'legislative_session__jurisdiction',
    )
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
    get_jurisdiction_name.short_description = 'Jurisdiction'

    def get_session_name(self, obj):
        return obj.legislative_session.name
    get_session_name.short_description = 'Session'
    get_session_name.admin_order_field = 'legislative_session__name'

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

    list_filter = ('legislative_session__jurisdiction__name',
                   )
