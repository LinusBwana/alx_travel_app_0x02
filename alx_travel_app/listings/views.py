from django.shortcuts import render
from rest_framework import viewsets
from .models import Property, Booking
from .serializers import PropertySerializer, BookingSerializer

# Create your views here.
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by('-created_at')
    serializer_class = PropertySerializer
    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-created_at')
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        property_pk = self.kwargs.get('property_pk') # from NestedDefaultRouter
        if property_pk:
            queryset = queryset.filter(property__property_id=property_pk)
        return queryset