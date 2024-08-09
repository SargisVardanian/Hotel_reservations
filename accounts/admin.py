from django.contrib import admin
from django.utils import timezone
from .models import Room, Booking


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0
    readonly_fields = ("user", "check_in", "check_out")

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price_per_night",
        "capacity",
        "is_available_today")
    search_fields = ("name",)
    ordering = ("name",)
    inlines = [BookingInline]

    def is_available_today(self, obj):
        today = timezone.now().date()
        return not obj.is_occupied_on_dates(today, today)

    is_available_today.boolean = True
    is_available_today.short_description = "Available Today"


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "room", "check_in", "check_out")
    search_fields = ("user__username", "room__name")
    ordering = ("check_in",)
    list_filter = ("check_in", "check_out")

    actions = ["cancel_booking"]

    def cancel_booking(self, request, queryset):
        queryset.delete()
        self.message_user(
            request,
            "Selected bookings have been cancelled and deleted.")

    cancel_booking.short_description = "Cancel and delete selected bookings"
