from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def contact(request):
    context = {
        'phonenumber': '999999',
        'tutor': 'Maria'
    }
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'contact.html', context)



'''
class ContatoForm(forms.Form): #forms.Form é padrão do django
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)

'''
# toda view precisa receber um parâmetro chamado request
# ele vai contar as informações sobre a requisição







