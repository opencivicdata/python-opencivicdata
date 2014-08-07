from django.contrib import admin
from django.template import defaultfilters


class LinkAdminInline(admin.TabularInline):
    fields = ('url', 'note')
    extra = 0


class LinkAdmin(admin.ModelAdmin):
    list_display = ('note', 'url')


class MimetypeLinkInline(admin.TabularInline):
    fields = ('media_type', 'url')
    extra = 0


class MimetypeLinkAdmin(admin.ModelAdmin):
    list_display = ('media',)


class IdentifierInline(admin.TabularInline):
    fields = ('identifier', 'scheme')
    extra = 0

class RelatedEntityInline(admin.TabularInline):
    fields = ('name', 'entity_type', 'organization', 'person')