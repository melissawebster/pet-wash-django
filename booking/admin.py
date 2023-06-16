from django.contrib import admin
from booking.models import Booking

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'pet_name', 'date']
    search_fields = ['pet_name']
    list_filter = ['date', 'shift', 'size']
