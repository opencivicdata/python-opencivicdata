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


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    pass


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
    list_display = ('organization', 'person', 'post', 'on_behalf_of',
        'label', 'role', 'start_date', 'end_date',)


@admin.register(models.MembershipContactDetail)
class MembershipContactDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MembershipLink)
class MembershipLinkAdmin(admin.ModelAdmin):
    pass


