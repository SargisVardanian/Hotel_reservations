# booking/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

    def is_available(self, check_in, check_out):
        overlapping_bookings = self.booking_set.filter(
            check_out__gt=check_in,
            check_in__lt=check_out
        )
        return not overlapping_bookings.exists()

    def is_available_in_period(self, start_date, end_date):
        return not self.booking_set.filter(
            check_out__gt=start_date,
            check_in__lt=end_date
        ).exists()

    def booking_status(self):
        today = timezone.now().date()
        current_booking = self.booking_set.filter(
            check_in__lte=today,
            check_out__gt=today
        ).first()

        next_booking = self.booking_set.filter(
            check_in__gt=today
        ).order_by('check_in').first()

        if current_booking:
            return f"Occupied: {current_booking.user.username} ({current_booking.check_in} - {current_booking.check_out})"
        elif next_booking:
            return f"Available until {next_booking.check_in}, then booked by {next_booking.user.username}"
        else:
            return "Available"

# class Booking(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     check_in = models.DateField()
#     check_out = models.DateField()
#
#     def __str__(self):
#         return f'{self.user.username} - {self.room.name}'
