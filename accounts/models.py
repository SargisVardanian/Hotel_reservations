from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

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


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='accounts_bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.room.name}'


class CustomUser(AbstractUser):
    pass
