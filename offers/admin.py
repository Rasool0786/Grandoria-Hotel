from django.contrib import admin

from .models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "room",
        "offer_price",
        "start_date",
        "end_date",
        "active",
        "is_current",
    )
    # list_filter = ("active", "start_date", "end_date", "room")
    # search_fields = ("title", "description", "room__title")
    readonly_fields = ("datetime_created", "datetime_updated")
    ordering = ("-start_date",)

    def is_current(self, obj):
        return obj.is_current()

    is_current.boolean = True
    is_current.short_description = "Is Current"
