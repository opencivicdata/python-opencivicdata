from django.contrib import admin
from django.template import defaultfilters
from opencivicdata.models import bill as models


@admin.register(models.BillAction)
class BillActionAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'bill', 'organization')
    list_selected_related = (
        'bill',
        'bill__legislative_session',
        'bill__legislative_session__jurisdiction')
    list_display = ('bill', 'date', 'description')


class BillActionInline(admin.TabularInline):
    model = models.BillAction
    readonly_fields = ('date', 'organization', 'description')
    fields = ('date', 'description', 'organization')
    extra = 0


class BillSponsorshipInline(admin.TabularInline):
    model = models.BillSponsorship
    readonly_fields = ('name',)
    fields = ('name', 'primary', 'classification')
    extra = 0


@admin.register(models.Bill)
class BillAdmin(admin.ModelAdmin):
    readonly_fields = ('from_organization', 'legislative_session')
    search_fields = ['identifier', 'title',]
    fields = (
        'identifier', 'legislative_session', 'classification',
        'from_organization', 'title', 'id', 'extras')
    list_selected_related = (
        'sources',
        'legislative_session',
        'legislative_session__jurisdiction')
    inlines = [BillActionInline, BillSponsorshipInline]

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


@admin.register(models.BillAbstract)
class BillAbstractAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BillTitle)
class BillTitleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BillIdentifier)
class BillIdentifierAdmin(admin.ModelAdmin):
    list_display = ('bill', 'identifier')
    readonly_fields = ('bill',)


@admin.register(models.BillActionRelatedEntity)
class BillActionRelatedEntityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RelatedBill)
class RelatedBillAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BillSponsorship)
class BillSponsorshipAdmin(admin.ModelAdmin):
    raw_id_fields = ('bill', 'person', 'organization')
    list_selected_related = (
        'person',
        'organization',
        'bill_legislative_session',
        'bill_legislative_session__jurisdiction')


@admin.register(models.BillDocument)
class BillDocumentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BillVersion)
class BillVersionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BillDocumentLink)
class BillDocumentLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BillVersionLink)
class BillVersionLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BillSource)
class BillSourceAdmin(admin.ModelAdmin):
    list_display = ('bill', 'url', 'note')
    readonly_fields = ('bill',)

