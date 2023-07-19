from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from booking.models import Booking, Branch
from rest_api.serializers import BookingModelSerializer, BranchModelSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class BranchModelViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookingModelViewSet(ModelViewSet):
    queryset = Booking.objects.all() 
    # faz o query no model, mas retorna um objeto
    serializer_class = BookingModelSerializer 
    #define qual serializer vai ser utilizado para tratar o objeto (e possibilitar um futuro json)
    authentication_classes = [TokenAuthentication] 
    #lista para aceitar as autenticações baseadas em token
    permission_classes = [IsAuthenticatedOrReadOnly] 
    #lista que vai autenticar as permissões que a views possui, só os usuários autenticados vão gerar endpoints pra api


@api_view(['GET', 'POST']) #essa api pode ser acessada pelos métodos get e post
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'hello': 'world API'})

