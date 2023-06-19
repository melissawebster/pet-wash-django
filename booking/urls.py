from django.urls import path
from booking.views import create

app_name = 'booking'
urlpatterns = [
    path('create/', create, name='create_booking')
]