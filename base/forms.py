from django import forms
from base.models import Contact #Booking

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


# class DateInput(forms.DateInput):
#     input_type = 'date'


# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['petname', 'cellphone', 'bathday', 'comments']
#         widgets = {
#             'bathday': DateInput(),
#         }
