from django.urls import path
from .views import home, mensaje, productos, login, registro

urlpatterns = [
    path('', home, name='home'),
    path('productos/', productos, name='productos'),
    path('mensajes/', mensaje, name='mensajes'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro')
]
