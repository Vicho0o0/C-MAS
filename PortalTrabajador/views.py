from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth import *
from django.contrib import messages
from django.conf import settings
from PortalCMAS.models import RegistroEntrada, MetricasCliente, TipoEjercicio, GrupoMuscular, Ejercicios, MetricasEjerciciosCliente, Perfil
from PortalCMAS.models import Clases, Membresias
from PortalCMAS.forms import *
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from random import randrange
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from django.utils.timezone import now

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

def Progreso_Trabajador(request):
    return render(request, 'Progreso_Trabajador.html')

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
    tipo_ejercicio=TipoEjercicio.objects.get(id=id)
    form=AgregarTipoEjercicioForm(instance=tipo_ejercicio)
    if request.method=="POST":
        form=AgregarTipoEjercicioForm(request.POST,instance=tipo_ejercicio)
        if form.is_valid():
            form.save()
        return Tipo_Ejercicio(request)
    data={'form':form,'titulo':'Actualizar Tipo de Ejercicio'}
    return render(request,'tipoejercicio_save.html',data)

def Delete_Tipo_Ejercicio(request, id):
    try:
        tipo_ejercicio=TipoEjercicio.objects.get(id=id)
    except TipoEjercicio.DoesNotExist:
        return redirect('../Tipo_Ejercicio/')

    if request.method == 'POST':
        tipo_ejercicio.delete()
        return redirect('../Tipo_Ejercicio/')
    
    return render(request, 'tipoejercicio_eliminar.html', {'tipo_ejercicio': tipo_ejercicio})

def Grupo_Muscular(request):
    grupo_muscular=GrupoMuscular.objects.all()
    data={'grupo_muscular':grupo_muscular,}
    return render(request, 'grupo_muscular.html',data)

def Agregar_Grupo_Muscular(request):
    form=AgregarGrupoMuscularForm()
    if request.method=='POST':
        form=AgregarGrupoMuscularForm(request.POST)
        if form.is_valid():
            form.save()
        return Grupo_Muscular(request)
    data={'form':form,'titulo':'Agregar Grupo Muscular'}
    return render(request,'grupomuscular_save.html',data)

def Actualizar_Grupo_Muscular(request, id):
    grupo_muscular=GrupoMuscular.objects.get(id=id)
    form=AgregarTipoEjercicioForm(instance=grupo_muscular)
    if request.method=="POST":
        form=AgregarTipoEjercicioForm(request.POST,instance=grupo_muscular)
        if form.is_valid():
            form.save()
        return Grupo_Muscular(request)
    data={'form':form,'titulo':'Actualizar Grupo Muscular'}
    return render(request,'grupomuscular_save.html',data)

def Delete_Grupo_Muscular(request, id):
    try:
        grupo_muscular=GrupoMuscular.objects.get(id=id)
    except GrupoMuscular.DoesNotExist:
        return redirect('../Grupo_Muscular/')

    if request.method == 'POST':
        grupo_muscular.delete()
        return redirect('../Grupo_Muscular/')
    
    return render(request, 'grupomuscular_delete.html', {'grupo_muscular': grupo_muscular})

def Ejercicio(request):
    ejercicios=Ejercicios.objects.all()
    data={'ejercicios':ejercicios,}
    return render(request, 'ejercicios.html',data)

def Agregar_Ejercicio(request):
    form=EjerciciosForm()
    if request.method=='POST':
        form=EjerciciosForm(request.POST)
        if form.is_valid():
            form.save()
        return Ejercicio(request)
    data={'form':form,'titulo':'Agregar Ejercicio'}
    return render(request,'ejercicios_save.html',data)

def Actualizar_Ejercicio(request, id):
    ejercicios=Ejercicios.objects.get(id=id)
    form=EjerciciosForm(instance=ejercicios)
    if request.method=="POST":
        form=EjerciciosForm(request.POST,instance=ejercicios)
        if form.is_valid():
            form.save()
        return Ejercicio(request)
    data={'form':form,'titulo':'Actualizar ejercicio'}
    return render(request,'ejercicios_save.html',data)

def Delete_Ejercicio(request, id):
    try:
        ejercicios=Ejercicios.objects.get(id=id)
    except Ejercicios.DoesNotExist:
        return redirect('../Ejercicios/')

    if request.method == 'POST':
        ejercicios.delete()
        return redirect('../Ejercicios/')
    
    return render(request, 'ejercicios_delete.html', {'grupo_muscular': ejercicios})

def RegistroEntrada(request):
    mensaje = None

    if request.method == "POST":
        rut = request.POST.get("rut")
        try:
            perfil = Perfil.objects.get(rut=rut)
            hoy = now().date()
            existe_registro = RegistroEntrada.objects.filter(
                perfil=perfil, hora_entrada__date=hoy
            ).exists()

            if existe_registro:
                mensaje = f"El usuario {perfil.user.first_name} {perfil.user.last_name} ya registró su entrada hoy."
            else:
                RegistroEntrada.objects.create(perfil=perfil, hora_entrada=now())
                mensaje = f"Acceso registrado para {perfil.user.first_name} {perfil.user.last_name}."
        except Perfil.DoesNotExist:
            mensaje = "El RUT ingresado no está registrado."

    registros = RegistroEntrada.objects.all().order_by("-hora_entrada")

    return render(request, "registro_entrada.html", {"mensaje": mensaje, "registros": registros})