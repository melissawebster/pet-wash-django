from django.shortcuts import render
from django.http import HttpResponse
from base.forms import ContactForm, BookingForm
from base.models import Contact, Booking

#sempre que se quer criar uma pagina em branco, tem que vir nas views

def index(request):
    return render(request, 'index.html')


def AboutUs(request):
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





