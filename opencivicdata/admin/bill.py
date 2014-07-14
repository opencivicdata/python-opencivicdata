from django.contrib import admin
from opencivicdata.models import bill as models


@admin.register(models.Bill)
class BillAdmin(admin.ModelAdmin):
    pass


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
    pass


@admin.register(models.Meta)
class MetaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BillActionRelatedEntity)
class BillActionRelatedEntityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RelatedBill)
class RelatedBillAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BillSponsorship)
class BillSponsorshipAdmin(admin.ModelAdmin):
    pass


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
    pass

