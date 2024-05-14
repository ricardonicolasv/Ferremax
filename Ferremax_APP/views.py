from django.shortcuts import render

# Create your views here.

# Pagina principal de la aplicacion
def home(request):
    # Lógica de la vista
    return render(request, 'home.html')
# Pagina de los productos de la tienda
def productos(request):
    #Logica de la vista
    return render(request, 'productos.html') 
# Pagina de los mensajes de la tienda
def mensaje(request):
    #Logica de la vista
    return render(request, 'mensaje.html') 
def login(request):
    #Logica de la vista
    return render(request, 'login.html') 
def registro(request):
    #Logica de la vista
    return render(request, 'registro.html') 
