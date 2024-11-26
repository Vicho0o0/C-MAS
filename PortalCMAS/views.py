from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth import *
from django.contrib import messages
from django.conf import settings
from .models import Schedule, Cliente, RegistroEntrada
from PortalCMAS.models import Clases, Membresias
from .forms import RegistroEntradaForm, MetricasClienteForm, MetricasTrenSuperiorForm, MetricasTrenInferiorForm, ClasesForm, FormLogin, MembresiasForm, FormRegistro
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from random import randrange

def Index(request):
    return render(request, 'index.html')

def MembresiasUsuarios(request):
    membresias=Membresias.objects.all()
    data={'membresias':membresias}
    return render(request, 'PortalMembresias.html',data)

def MembresiasAdmin(request):
    membresias=Membresias.objects.all()
    data={'membresias':membresias}
    return render(request, 'PortalMembresiasAdmin.html',data)

def CrearMembresias(request):
    form=MembresiasForm()
    if request.method=='POST':
        form=MembresiasForm(request.POST)
        if form.is_valid():
            form.save()
        return MembresiasAdmin(request)
    data={'form':form,'titulo':'Agregar Membresia'}
    return render(request,'membresias_crear.html',data)

def Eliminar_Membresia(request, id):
    try:
        membresias = Membresias.objects.get(id=id)
    except Membresias.DoesNotExist:
        return redirect('../MembresiasAdmin/')

    if request.method == 'POST':
        membresias.delete()
        return redirect('../MembresiasAdmin/')
    
    return render(request, 'membresias_eliminar.html', {'membresias': membresias})

def Actualizar_Membresia(request,id):
    membresias=Membresias.objects.get(id=id)
    form=MembresiasForm(instance=membresias)
    if request.method=="POST":
        form=MembresiasForm(request.POST,instance=membresias)
        if form.is_valid():
            form.save()
        return MembresiasAdmin(request)
    data={'form':form,'titulo':'Actualizar Membresia'}
    return render(request,'membresias_crear.html',data)

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

def Clases_profesor(request):
    clases=Clases.objects.all()
    data={'clases':clases}
    return render(request, 'clases_profesor.html',data)

def Crear_Clase(request):
    form=ClasesForm()
    if request.method=='POST':
        form=ClasesForm(request.POST)
        if form.is_valid():
            form.save()
        return Clases_profesor(request)
    data={'form':form,'titulo':'Agregar Clases'}
    return render(request,'clases_save.html',data)

def Ver_Clase(request,id):
    clases=Clases.objects.get(id=id)
    data={"clases":clases}
    return render(request,'clases_ver.html',data)

def Actualizar_Clase(request,id):
    clases=Clases.objects.get(id=id)
    form=ClasesForm(instance=clases)
    if request.method=="POST":
        form=ClasesForm(request.POST,instance=clases)
        if form.is_valid():
            form.save()
        return Clases_profesor(request)
    data={'form':form,'titulo':'Actualizar Clase'}
    return render(request,'clases_save.html',data)


def Eliminar_Clase(request, id):
    try:
        clases = Clases.objects.get(id=id)
    except Clases.DoesNotExist:
        return redirect('../Clases_profesor/')

    if request.method == 'POST':
        clases.delete()
        return redirect('../Clases_profesor/')
    
    return render(request, 'clases_eliminar.html', {'clases': clases})

def Login_Admin(request):
    return render(request, 'PortalAdministrativo.html')

def ProgresoCliente(request):
    return render(request, 'metricas_progreso.html')

def GraficoCliente(request):
    return render(request, 'graficos_cliente.html')

def get_chart(request):
    serie=[]
    counter=0
    while(counter<6):
        serie.append(randrange(100,400))
        counter += 1
    chart = {
        'xAxis': [
            {
                'type':"category",
                'data': ["Lunes","Martes","Miercoles","jueves","Viernes","Sábado"]
            }
        ],
        'yAxis': [
            {
                'type':"value",

            }
        ],
        'series':[
            {
                'data':serie,
                'type':"line"
            }
        ]
        
    }

    return JsonResponse(chart)

def Metricas_cliente(request):
    form=MetricasClienteForm()
    if request.method=='POST':
        form=MetricasClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return ProgresoCliente(request)
    data={'form':form,'titulo':'Agregar Medidas'}
    return render(request,'metricas_cliente.html',data)

def Metricas_TrenSuperior(request):
    form=MetricasTrenSuperiorForm()
    if request.method=='POST':
        form=MetricasTrenSuperiorForm(request.POST)
        if form.is_valid():
            form.save()
        return ProgresoCliente(request)
    data={'form':form,'titulo':'Agregar Medidas'}
    return render(request,'metricas_trensuperior.html',data)

def Metricas_TrenInferior(request):
    form=MetricasTrenInferiorForm()
    if request.method=='POST':
        form=MetricasTrenInferiorForm(request.POST)
        if form.is_valid():
            form.save()
        return ProgresoCliente(request)
    data={'form':form,'titulo':'Agregar Medidas'}
    return render(request,'metricas_treninferior.html',data)

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

def Inscripcion(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    return redirect('success_page') 

def RegistroEntrada(request): 
    cliente = None
    error = None

    if request.method == 'POST':
        form = RegistroEntradaForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            try:
                cliente = Cliente.objects.get(rut=rut)
                RegistroEntrada.objects.create(cliente=cliente, hora_entrada=now())
                messages.success(request, f"Acceso registrado para {cliente.nombre} {cliente.apellido}.")
                return redirect('registro_entrada')
            except Cliente.DoesNotExist:
                error = "El RUT ingresado no está registrado."
        else:
            error = "El formulario contiene datos inválidos."
    else:
        form = RegistroEntradaForm()

    return render(request, 'registro_entrada.html', {'form': form, 'cliente': cliente, 'error': error})