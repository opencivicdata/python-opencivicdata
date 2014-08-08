from django.core import urlresolvers
from django.contrib import admin
from opencivicdata.models import people_orgs as models

from opencivicdata.admin.base import (
    IdentifierInline, LinkAdmin
    )


class OrganizationIdentifierInline(IdentifierInline):
    model = models.OrganizationIdentifier


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    readonly_fields = ('parent', 'jurisdiction')
    fields = (
        'name', 'jurisdiction', 'id', 'classification',
        'parent', ('founding_date', 'dissolution_date'),
        'image', 'extras')
    list_display = ('name', 'jurisdiction')
    inlines = [
        OrganizationIdentifierInline
        ]


@admin.register(models.OrganizationIdentifier)
class OrganizationIdentifierAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrganizationName)
class OrganizationNameAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrganizationContactDetail)
class OrganizationContactDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrganizationLink)
class OrganizationLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrganizationSource)
class OrganizationSourceAdmin(LinkAdmin):
    list_display = ('organization', 'note', 'url')


@admin.register(models.PostContactDetail)
class PostContactDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PostLink)
class PostLinkAdmin(admin.ModelAdmin):
    pass


class PersonMembershipInline(admin.TabularInline):
    model = models.Membership
    readonly_fields = ('organization', 'post')
    fields = ('organization', 'post', 'label', 'role')
    extra = 0


class PersonIdentifierInline(IdentifierInline):
    model = models.PersonIdentifier


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ['name']
    fields = (
        'name', 'id', 'image',
        ('birth_date', 'death_date'),
        'biography', 'extras',
        ('gender', 'national_identity', 'sort_name', 'summary'))

    list_selected_related = (
        'memberships',
        )
    inlines = [PersonMembershipInline, PersonIdentifierInline]

    def get_memberships(self, obj):
        memberships = obj.memberships.select_related('organization__jurisdiction')
        html = []
        SHOW_N = 5
        for memb in memberships[:SHOW_N]:
            info = (memb._meta.app_label, memb._meta.module_name)
            admin_url = urlresolvers.reverse('admin:%s_%s_change' % info, args=(memb.pk,))
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

    list_display = ('name', 'id', 'get_memberships')


@admin.register(models.PersonIdentifier)
class PersonIdentifierAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PersonName)
class PersonNameAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PersonContactDetail)
class PersonContactDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PersonLink)
class PersonLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PersonSource)
class PersonSourceAdmin(LinkAdmin):
    list_display = ('person', 'note', 'url')


@admin.register(models.Membership)
class MembershipAdmin(admin.ModelAdmin):
    readonly_fields = ('organization', 'person', 'post', 'on_behalf_of')
    list_display = ('organization', 'person', 'post', 'on_behalf_of',
        'label', 'role', 'start_date', 'end_date',)
    fields = ('organization', 'person', 'role', 'post', 'on_behalf_of',
        'label', ('start_date', 'end_date'), 'extras')


@admin.register(models.MembershipContactDetail)
class MembershipContactDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MembershipLink)
class MembershipLinkAdmin(admin.ModelAdmin):
    pass


