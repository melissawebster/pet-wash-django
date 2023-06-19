from django.shortcuts import render
from booking.forms import BookingForm

def create(request):
    success = False
    form = BookingForm(request.POST or None)

    if form.is_valid(): 
        success = True
        form.save()

    responsible = {
        'form': form,
        'success': success
    }
    
    return render(request, 'create.html', responsible)
