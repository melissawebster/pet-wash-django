from django import forms
from booking.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'name', 'email', 'pet_name', 'date', 'shift', 'size', 'notes'
        ]