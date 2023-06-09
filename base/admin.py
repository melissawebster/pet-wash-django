from django.contrib import admin
from base.models import Contact, Booking

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'data']
    search_fields = ['name', 'email']
    list_filter = ['data']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
