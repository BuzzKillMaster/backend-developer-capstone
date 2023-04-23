from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
