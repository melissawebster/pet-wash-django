from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


# toda view precisa receber um parâmetro chamado request
# ele vai contar as informações sobre a requisição
