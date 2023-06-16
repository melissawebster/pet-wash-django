from django.contrib import admin
from base.models import Contact, Booking
from django.contrib import messages

@admin.action(description='Mark contact form as read')
def mark_as_read(modeladmin, request, queryset):
    queryset.update(read=True)
    modeladmin.message_user(request, 'Contact form marked as read', messages.SUCCESS)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'data', 'read']
    search_fields = ['name', 'email']
    list_filter = ['data', 'read']
    actions = [mark_as_read]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
