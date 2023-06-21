from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from booking.models import Booking
from rest_api.serializers import BookingModelSerializer

class BookingModelViewSet(ModelViewSet):
    queryset = Booking.objects.all() # faz o query no model, mas retorna um objeto
    serializer_class = BookingModelSerializer #define qual serializer vai ser utilizado para tratar o objeto (e possibilitar um futuro json)

@api_view(['GET', 'POST']) #essa api pode ser acessada pelos métodos get e post
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'hello': 'world API'})

