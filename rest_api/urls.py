from django.urls import path
from rest_api.views import hello_world, BookingModelViewSet, BranchModelViewSet
from rest_framework.routers import SimpleRouter


app_name = 'rest_api'
router = SimpleRouter(trailing_slash=False) #False pra nao adicionar barra no final da URL
router.register('booking', BookingModelViewSet)
router.register('branch', BranchModelViewSet)


urlpatterns = [
    path('hello_world', hello_world, name='hello_world_api'),
]

urlpatterns += router.urls
