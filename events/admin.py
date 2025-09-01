from django.contrib import admin

from .models import Event, EventImage


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'datetime_updated')
    search_fields = ('title', 'description', 'location')
    list_filter = ('date',)
    inlines = [EventImageInline]
    
    
@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display = ('event', 'image')
    search_fields = ('event__title',)