from rest_framework import viewsets, filters, permissions
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.forms import DateInput
from django_filters import rest_framework as filterss
from django.utils.translation import gettext_lazy as _

class DateInput(DateInput):
    input_type = 'date'

class RoomFilter(filterss.FilterSet):
    min_price = filterss.NumberFilter(field_name="price_per_night", lookup_expr='gte', label=_("Minimum price per night"))
    max_price = filterss.NumberFilter(field_name="price_per_night", lookup_expr='lte', label=_("Maximum price per night"))
    check_in = filterss.DateFilter(method='filter_available', widget=DateInput(attrs={'type': 'date'}), label=_("Check-in date"))
    check_out = filterss.DateFilter(method='filter_available', widget=DateInput(attrs={'type': 'date'}), label=_("Check-out date"))

    class Meta:
        model = Room
        fields = ['capacity', 'min_price', 'max_price', 'check_in', 'check_out']
        labels = {
            'capacity': _("Capacity"),
        }

    def filter_available(self, queryset, name, value):
        check_in = self.form.cleaned_data.get('check_in')
        check_out = self.form.cleaned_data.get('check_out')

        if check_in and check_out:
            occupied_rooms = Booking.objects.filter(
                check_in__lt=check_out, check_out__gt=check_in
            ).values_list('room_id', flat=True)
            return queryset.exclude(id__in=occupied_rooms)
        return queryset

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = RoomFilter
    ordering_fields = ['price_per_night', 'capacity']

    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price:
            queryset = queryset.filter(price_per_night__gte=min_price)
        if max_price:
            queryset = queryset.filter(price_per_night__lte=max_price)

        return queryset

    @action(detail=False, methods=['get'])
    def available(self, request):
        check_in = request.query_params.get('check_in')
        check_out = request.query_params.get('check_out')

        queryset = self.get_queryset()

        if check_in and check_out:
            try:
                check_in = timezone.datetime.strptime(check_in, '%Y-%m-%d').date()
                check_out = timezone.datetime.strptime(check_out, '%Y-%m-%d').date()
            except ValueError:
                return Response({"error": "Dates must be in YYYY-MM-DD format."})

            if check_in >= check_out:
                return Response({"error": "check_in date must be before check_out date."})

            occupied_rooms = Booking.objects.filter(
                check_in__lt=check_out, check_out__gt=check_in
            ).values_list('room_id', flat=True)
            queryset = queryset.exclude(id__in=occupied_rooms)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
