from django.contrib import admin

# Helpers ##########


class ModelAdmin(admin.ModelAdmin):
    """ deletion of top level objects is evil """

    actions = None

    def has_delete_permission(self, request, obj=None):
        return False

    # we probably don't want to add anything through the interface
    def has_add_permission(self, request):
        return False

    # To ignore `DisallowedModelAdminLookup` error because of non
    # registered models
    def lookup_allowed(self, request, key):
        return True


class ReadOnlyTabularInline(admin.TabularInline):
    def has_add_permission(self, request):
        return False

    can_delete = False


class IdentifierInline(admin.TabularInline):
    fields = readonly_fields = ("identifier", "scheme")
    extra = 0
    can_delete = False
    verbose_name = "ID from another system"
    verbose_name_plural = "IDs from other systems"

    def has_add_permission(self, request):
        return False


class LinkInline(admin.TabularInline):
    fields = ("url", "note")
    extra = 0


class ContactDetailInline(admin.TabularInline):
    fields = ("type", "value", "note", "label")
    extra = 0
    verbose_name = "Piece of contact information"
    verbose_name_plural = "Contact information"


class OtherNameInline(admin.TabularInline):
    extra = 0
    verbose_name = "Alternate name"
    verbose_name_plural = "Alternate names"


class MimetypeLinkInline(admin.TabularInline):
    fields = ("media_type", "url")


class RelatedEntityInline(admin.TabularInline):
    fields = ("name", "entity_type", "organization", "person")
