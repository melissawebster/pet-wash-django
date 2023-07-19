from django import forms
from booking.models import Booking
import datetime

class BookingForm(forms.ModelForm):
    def clean_data(self):
        Date = self.cleaned_data['date']
        today = datetime.date.today()
        if Date < today:
            raise forms.ValidationError('You cannot book a bath on a day from the past.')
        return Date

    class Meta:
        model = Booking
        fields = [
            'name', 'email', 'pet_name', 'date', 'shift', 'branch', 'size', 'notes'
        ]