from django.shortcuts import render

# Create your views here.

# Pagina principal de la aplicacion
def home(request):
    # Lógica de la vista
    return render(request, 'home.html')
# Pagina de los productos de la tienda
def herramientas(request):
    #Logica de la vista
    return render(request, 'herramientas.html') 
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
def materiales(request):
    #Logica de la vista
    return render(request, 'materiales.html') 
def electricidad(request):
    #Logica de la vista
    return render(request, 'electricidad.html') 
def plomeria(request):
    #Logica de la vista
    return render(request, 'plomeria.html') 