from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import ProductoForm
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
def materiales(request):
    #Logica de la vista
    return render(request, 'materiales.html') 
def electricidad(request):
    #Logica de la vista
    return render(request, 'electricidad.html') 
def plomeria(request):
    #Logica de la vista
    return render(request, 'plomeria.html') 
def home(request):
    return render (request, 'home.html')

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre_completo = form.cleaned_data.get('nombre_completo')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirmar_password = form.cleaned_data.get('confirmar_password')

            # Verifica que las contraseñas ingresadas sean iguales
            if password != confirmar_password:
                return render(request, 'registrar.html', {
                    'form': RegistroForm(),
                    'error': 'Las contraseñas no coinciden.'
                })

            try:
                user = User.objects.create_user(username=email, email=email, password=password, first_name=nombre_completo)
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registrar.html', {
                    'form': RegistroForm(),
                    'error': 'El correo electrónico ya está registrado.'
                })
    else:
        form = RegistroForm()
    return render(request, 'registrar.html', {'form': form})

def tasks(request):
    return render (request, 'tasks.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def ingresar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Maneja el caso en que el usuario no esté registrado, la contraseña sea incorrecta
                # o el correo electrónico esté mal formateado
                return render(request, 'ingresar.html', {
                    'form': form,
                    'error': 'Correo electrónico o contraseña incorrectos.'
                })
        else:
            # Maneja el caso en que el correo electrónico esté mal formateado
            return render(request, 'ingresar.html', {
                'form': form,
                'error': 'Por favor ingrese un correo electrónico válido.'
            })
    else:
        form = AuthenticationForm()
    return render(request, 'ingresar.html', {'form': form})

def ingresar_productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingresarproductos')
    else:
        form = ProductoForm()
    return render(request, 'ingresarproductos.html', {'form': form})