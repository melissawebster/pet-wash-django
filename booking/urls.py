from django.urls import path
from booking.views import create_booking

app_name = 'booking'
urlpatterns = [
    path('create/', create_booking, name='create booking')
]