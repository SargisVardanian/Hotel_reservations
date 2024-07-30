# booking/serializers.py
from rest_framework import serializers
from .models import Room, Booking
from django.utils import timezone

class RoomSerializer(serializers.ModelSerializer):
    is_available = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ['id', 'name', 'price_per_night', 'capacity', 'is_available']

    def get_is_available(self, obj):
        request = self.context.get('request')
        check_in = request.query_params.get('check_in')
        check_out = request.query_params.get('check_out')
        if check_in and check_out:
            check_in = timezone.datetime.strptime(check_in, '%Y-%m-%d').date()
            check_out = timezone.datetime.strptime(check_out, '%Y-%m-%d').date()
            return obj.is_available(check_in, check_out)
        return True

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
