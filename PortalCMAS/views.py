from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth import *
from django.contrib import messages
from django.conf import settings
from .models import Schedule, Cliente, RegistroEntrada
from PortalCMAS.models import Clases, Membresias, GrupoMuscular, Ejercicios
from .forms import *

from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse
from random import randrange
from django.utils.timezone import now
from django.views.decorators.http import require_http_methods
from .forms import RegistroEntradaForm
from .models import Perfil, RegistroEntrada

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
                return redirect('../Portal_Trabajador/')
            else:
                messages.error(request, "Credenciales incorrectas o usuario sin permisos.")
        except User.DoesNotExist:
            messages.error(request, "RUT no encontrado.")
            
    return render(request, 'PortalAdministrativo.html')

@login_required
def ProgresoCliente(request):
    hoy = now().date()
    metricas_hoy = MetricasCliente.objects.filter(
        rut_cliente=request.user.perfil.rut,
        fecha_marca__date=hoy
    ).exists()
    
    ejercicios_hoy = MetricasEjerciciosCliente.objects.filter(
        rut_cliente=request.user.perfil.rut,
        fecha_marca__date=hoy
    ).exists()

    if request.method == 'POST':
        if 'submit_metricas' in request.POST:
            if metricas_hoy:
                messages.warning(request, "Ya has registrado tus métricas hoy. Solo puedes registrar una vez al día.")
                return redirect('progreso')
            
            form_metricas = MetricasClienteForm(request.POST)
            if form_metricas.is_valid():
                metrica = form_metricas.save(commit=False)
                metrica.rut_cliente = request.user.perfil.rut
                metrica.save()
                messages.success(request, "Métricas guardadas exitosamente")
                return redirect('progreso')
                
        elif 'submit_ejercicios' in request.POST:
            if ejercicios_hoy:
                messages.warning(request, "Ya has registrado tus ejercicios hoy. Solo puedes registrar una vez al día.")
                return redirect('progreso')
            
            form_ejercicios = MetricasEjerciciosClienteForm(request.POST)
            if form_ejercicios.is_valid():
                ejercicio = form_ejercicios.save(commit=False)
                ejercicio.rut_cliente = request.user.perfil.rut
                ejercicio.save()
                messages.success(request, "Ejercicio registrado exitosamente")
                return redirect('progreso')

    context = {
        'form_metricas': MetricasClienteForm() if not metricas_hoy else None,
        'form_ejercicios': MetricasEjerciciosClienteForm() if not ejercicios_hoy else None,
        'metricas': MetricasCliente.objects.filter(rut_cliente=request.user.perfil.rut).order_by('-fecha_marca'),
        'ejercicios': MetricasEjerciciosCliente.objects.filter(rut_cliente=request.user.perfil.rut).order_by('-fecha_marca'),
        'metricas_hoy': metricas_hoy,
        'ejercicios_hoy': ejercicios_hoy
    }
    
    return render(request, 'metricas_progreso.html', context)

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

def registro_entrada_view(request):
    mensaje = None
    form = RegistroEntradaForm()

    if request.method == "POST":
        form = RegistroEntradaForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            try:
                perfil = Perfil.objects.get(rut=rut)
                hoy = now().date()
                existe_registro = RegistroEntrada.objects.filter(
                    perfil=perfil, 
                    hora_entrada__date=hoy
                ).exists()

                if existe_registro:
                    mensaje = f"El usuario {perfil.user.first_name} {perfil.user.last_name} ya registró su entrada hoy."
                else:
                    RegistroEntrada.objects.create(perfil=perfil, hora_entrada=now())
                    mensaje = f"Acceso registrado para {perfil.user.first_name} {perfil.user.last_name}."
            except Perfil.DoesNotExist:
                mensaje = "El RUT ingresado no está registrado."

    registros = RegistroEntrada.objects.all().order_by("-hora_entrada")[:10]

    return render(request, "registro_entrada.html", {
        "form": form,
        "mensaje": mensaje, 
        "registros": registros
    })

@login_required
def GestionEjercicios(request):
    tipos_ejercicio = TipoEjercicio.objects.all()
    grupos_musculares = GrupoMuscular.objects.all()
    ejercicios = Ejercicios.objects.all()
    
    context = {
        'tipos_ejercicio': tipos_ejercicio,
        'grupos_musculares': grupos_musculares,
        'ejercicios': ejercicios
    }
    return render(request, 'gestion_ejercicios.html', context)

def Actualizar_Tipo_Ejercicio(request, id):
    tipo_ejercicio = get_object_or_404(TipoEjercicio, id=id)
    
    if request.method == 'POST':
        form = FormTipoEjercicio(request.POST, instance=tipo_ejercicio)
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo de ejercicio actualizado exitosamente.")
            return redirect('tipo_ejercicio')
    else:
        form = FormTipoEjercicio(instance=tipo_ejercicio)

    context = {
        'form': form,
        'titulo': 'Actualizar Tipo de Ejercicio'
    }
    return render(request, 'tipoejercicio_save.html', context)