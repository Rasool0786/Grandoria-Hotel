from django.contrib import admin

from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'rating', 'active', 'datetime_updated')
    list_filter = ('active', 'rating', 'datetime_created')
    search_fields = ('author__username', 'role', 'message')
    ordering = ('-datetime_created',)
    readonly_fields = ('datetime_created', 'datetime_updated')