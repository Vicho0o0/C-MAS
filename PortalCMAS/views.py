from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth import *
from django.contrib import messages
from django.conf import settings
from .models import Schedule, Cliente, RegistroEntrada
from PortalCMAS.models import Clases, Membresias
from .forms import *

from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse
from random import randrange

def IndexC(request):
    return render(request, 'indexC.html')

def MembresiasUsuarios(request):
    membresias=Membresias.objects.all()
    data={'membresias':membresias}
    return render(request, 'PortalMembresias.html',data)

def Login(request):
    if request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(perfil__rut=rut)
                if user.password == password:
                    login(request, user)
                    return redirect('../')
                else:
                    messages.error(request, "Contraseña incorrecta.")
            except User.DoesNotExist:
                messages.error(request, "RUT no encontrado.")
    else:
        form = FormLogin()
    return render(request, 'PortalLogin.html', {'form': form})

def Registro(request):
    if request.method == "POST":
        form = FormRegistro(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password1']
            user.save()
            user.perfil.rut = form.cleaned_data.get('rut')
            user.perfil.save()
            messages.success(request, "Registro Exitoso. Puedes iniciar sesión ahora.")
            return redirect('../PortalLogin')
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = FormRegistro()

    return render(request, 'PortalRegistro.html', {"form": form})


def Clases_cliente(request):
    clases=Clases.objects.all()
    data={'clases':clases}
    return render(request, 'clases_clientes.html',data)

def Inscripcion(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    return redirect('success_page') 

def Login_Admin(request):
    if request.method == "POST":
        rut = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(perfil__rut=rut)
            if user.password == password and user.is_staff:
                login(request, user)
                messages.success(request, "Inicio de sesión exitoso.")
                return redirect('../')
            else:
                messages.error(request, "Credenciales incorrectas o usuario sin permisos.")
        except User.DoesNotExist:
            messages.error(request, "RUT no encontrado.")
            
    return render(request, 'PortalAdministrativo.html')

def ProgresoCliente(request):
    return render(request, 'metricas_progreso.html')

def GraficoCliente(request):
    return render(request, 'graficos_cliente.html')

def get_chart(request):
    serie = [randrange(100, 400) for _ in range(6)]
    chart = {
        'xAxis': [
            {
                'type': "category",
                'data': ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
            }
        ],
        'yAxis': [
            {
                'type': "value",
            }
        ],
        'series': [
            {
                'data': serie,
                'type': "line"
            }
        ]
    }
    return JsonResponse(chart)

def Comunidad(request):
    return render(request, 'comunidad.html')

def Contactos(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        correo = request.POST.get('email')
        mensaje = request.POST.get('message')
        
        send_mail(
            f"Mensaje de {nombre}",
            mensaje,
            correo, 
            [settings.EMAIL_HOST_USER], 
            fail_silently=False,
        )
        return render(request, 'contacto.html', {'mensaje_enviado': True})
    return render(request, 'contacto.html')