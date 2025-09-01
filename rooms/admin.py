from django.contrib import admin

from .models import Room, Reservation, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'capacity', 'active', 'room_type', 'author', 'datetime_created', 'datetime_updated')
    list_filter = ('active', 'room_type', 'author')
    search_fields = ('title', 'description', 'author__username')
    ordering = ('-datetime_created',)
    filter_horizontal = ('amenities',)
    readonly_fields = ('datetime_created', 'datetime_updated')
    
@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')
    search_fields = ('title', 'description')
    ordering = ('title',)
    
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'room', 'check_in', 'check_out', 'guests', 'status', 'datetime_created', 'datetime_updated')
    list_filter = ('status', 'room')
    search_fields = ('name', 'email', 'room__title')
    ordering = ('-datetime_created',)
    date_hierarchy = 'check_in'
    readonly_fields = ('datetime_created', 'datetime_updated')
