from django.shortcuts import render
from django.http import HttpResponse
from base.forms import ContactForm

#sempre que se quer criar uma pagina em branco, tem que vir nas views

def index(request):
    return render(request, 'index.html')

def contact(request):
    success = False
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            success= True

    responsible = {
        'responsible_number': '999999',
        'responsible_name': 'Maria',
        'form': form,
        'success': success
    }
    
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'contact.html', responsible)


def test(request):
    return render(request, 'test.html')




'''
class ContatoForm(forms.Form): #forms.Form é padrão do django
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)

'''
# toda view precisa receber um parâmetro chamado request
# ele vai contar as informações sobre a requisição







