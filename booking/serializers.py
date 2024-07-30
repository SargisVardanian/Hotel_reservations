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

    def validate(self, data):
        check_in = data['check_in']
        check_out = data['check_out']
        room = data['room']

        # Проверка, что дата заезда раньше даты выезда
        if check_in >= check_out:
            raise serializers.ValidationError("Check-in date must be before check-out date.")

        # Проверка, что комната доступна для бронирования на указанные даты
        if not room.is_available(check_in, check_out):
            raise serializers.ValidationError("Room is not available for the selected dates.")

        return data
