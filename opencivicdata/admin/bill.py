from django.contrib import admin
from opencivicdata.models import bill as models


@admin.register(models.Bill)
class BillAdmin(admin.ModelAdmin):

    raw_id_fields = ('from_organization',)

    list_selected_related = (
        'sources',
        'legislative_session',
        'legislative_session__jurisdiction')

    def source_link(self, obj):
        source = obj.sources.filter(url__icontains="legislationdetail").get()
        tmpl = u'<a href="{0}" target="_blank">View source</a>'
        return tmpl.format(source.url)
    source_link.short_description = 'View source'
    source_link.allow_tags = True

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
    pass


@admin.register(models.BillAction)
class BillActionAdmin(admin.ModelAdmin):
    raw_id_fields = ('bill', 'organization')
    list_selected_related = (
        'bill',
        'bill__legislative_session',
        'bill__legislative_session__jurisdiction')

    list_display = ('bill', 'date', 'description')


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

