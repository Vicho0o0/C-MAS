from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth import *
from django.contrib import messages
from django.conf import settings
from PortalCMAS.models import Schedule, Cliente, RegistroEntrada, MetricasCliente, TipoEjercicio, GrupoMuscular, Ejercicios, MetricasEjerciciosCliente
from PortalCMAS.models import Clases, Membresias
from PortalCMAS.forms import RegistroEntradaForm, ClasesForm, FormLogin, MembresiasForm, FormRegistro, AgregarTipoEjercicioForm
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from random import randrange
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login

# Create your views here.
def IndexT(request):
    return render(request, 'indexT.html')

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

def Tipo_Ejercicio(request):
    tipo_ejercicio=TipoEjercicio.objects.all()
    data={'tipo_ejercicio':tipo_ejercicio,}
    return render(request, 'tipo_ejercicio.html',data)

def Agregar_Tipo_Ejercicio(request):
    form=AgregarTipoEjercicioForm()
    if request.method=='POST':
        form=AgregarTipoEjercicioForm(request.POST)
        if form.is_valid():
            form.save()
        return Tipo_Ejercicio(request)
    data={'form':form,'titulo':'Agregar Tipo de Ejercicio'}
    return render(request,'tipoejercicio_save.html',data)

def Actualizar_Tipo_Ejercicio(request, id):
    clases=TipoEjercicio.objects.get(id=id)
    form=AgregarTipoEjercicioForm(instance=clases)
    if request.method=="POST":
        form=AgregarTipoEjercicioForm(request.POST,instance=clases)
        if form.is_valid():
            form.save()
        return Tipo_Ejercicio(request)
    data={'form':form,'titulo':'Actualizar Tipo de Ejercicio'}
    return render(request,'tipoejercicio_save.html',data)

def Delete_Tipo_Ejercicio(request, id):
    try:
        tipo_ejercicio=TipoEjercicio.objects.get(id=id)
    except Clases.DoesNotExist:
        return redirect('../Tipo_Ejercicio/')

    if request.method == 'POST':
        tipo_ejercicio.delete()
        return redirect('../Tipo_Ejercicio/')
    
    return render(request, 'tipoejercicio_eliminar.html', {'tipo_ejercicio': tipo_ejercicio})

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