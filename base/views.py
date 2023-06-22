from django.shortcuts import render
from django.http import HttpResponse
from base.forms import ContactForm
from base.models import Contact, Booking
from booking.forms import BookingForm

def index(request):
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about-us.html')


def contact(request):
    success = False
    form = ContactForm(request.POST or None)

    if form.is_valid(): 
        success = True
        form.save()

    responsible = {
        'responsible_number': '(99) 8877-6655',
        'responsible_name': 'Melissa',
        'form': form,
        'success': success
    }
    
    return render(request, 'contact.html', responsible)


def login(request):
    return render(request, 'login.html')

def create_booking(request):
    success = False
    form = BookingForm(request.POST or None)

    if form.is_valid(): 
        success = True
        form.save()

    responsible = {
        'form': form,
        'success': success
    }
    
    return render(request, 'create-booking.html', responsible)



