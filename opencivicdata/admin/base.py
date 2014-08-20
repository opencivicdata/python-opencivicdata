from django.contrib import admin
from django.template import defaultfilters


class ModelAdmin(admin.ModelAdmin):
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


#class MimetypeLinkInline(admin.TabularInline):
#    fields = ('media_type', 'url')
#class RelatedEntityInline(admin.TabularInline):
#    fields = ('name', 'entity_type', 'organization', 'person')
