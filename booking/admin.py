# booking/admin.py
from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_night', 'capacity', 'booking_status_info')
    search_fields = ('name',)
    ordering = ('name',)

    def booking_status_info(self, obj):
        return obj.booking_status()
    booking_status_info.short_description = 'Booking Status'

# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('user', 'room', 'check_in', 'check_out')
#     search_fields = ('user__username', 'room__name')
#     ordering = ('check_in',)
#     list_filter = ('check_in', 'check_out')
