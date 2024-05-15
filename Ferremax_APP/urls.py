from django.urls import path
from .views import home, mensaje, herramientas, login, registro, materiales, electricidad, plomeria

urlpatterns = [
    path('', home, name='home'),
    path('herramientas/', herramientas, name='herramientas'),
    path('mensajes/', mensaje, name='mensajes'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('materiales/', materiales, name='materiales'),
    path('electricidad/', electricidad, name='electricidad'),
    path('plomeria/', plomeria, name='plomeria'),
]
