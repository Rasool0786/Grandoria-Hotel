from django.contrib import admin

from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'size', 'datetime_created', 'active')
    list_filter = ('active', 'datetime_created')
    search_fields = ('title', 'description')
    ordering = ('-datetime_created',)
    readonly_fields = ('datetime_created', 'datetime_updated')