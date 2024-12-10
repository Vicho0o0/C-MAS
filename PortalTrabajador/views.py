from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth import *
from django.contrib import messages
from django.conf import settings
from PortalCMAS.models import RegistroEntrada, MetricasCliente, TipoEjercicio, GrupoMuscular, Ejercicios as ModeloEjercicio, MetricasEjerciciosCliente, Perfil
from PortalCMAS.models import Clases, Membresias
from PortalCMAS.forms import ClasesForm, MembresiasForm, AgregarTipoEjercicioForm, AgregarGrupoMuscularForm, EjerciciosForm, GrupoMuscularForm
from PortalTrabajador.forms import RegistroEntradaForm
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from random import randrange
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required

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

def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def registro_entrada(request):
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

def Progreso_Trabajador(request):

    metricas = MetricasCliente.objects.all().order_by('-fecha_marca')
    ejercicios = MetricasEjerciciosCliente.objects.all().order_by('-fecha_marca')
    
    context = {
        'metricas': metricas,
        'ejercicios': ejercicios
    }
    
    return render(request, 'progreso_trabajador.html', context)

def Grupo_Muscular(request):
    grupos = GrupoMuscular.objects.all()
    data = {'grupos': grupos}
    return render(request, 'grupo_muscular.html', data)

def Agregar_Grupo_Muscular(request):
    form = AgregarGrupoMuscularForm()
    if request.method == 'POST':
        form = AgregarGrupoMuscularForm(request.POST)
        if form.is_valid():
            form.save()
        return Grupo_Muscular(request)
    data = {
        'form': form,
        'titulo': 'Agregar Grupo Muscular'
    }
    return render(request, 'grupomuscular_save.html', data)

def Actualizar_Grupo_Muscular(request, id):
    grupo = GrupoMuscular.objects.get(id=id)
    form = GrupoMuscularForm(instance=grupo)
    if request.method == 'POST':
        form = GrupoMuscularForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('gestion_ejercicios')
    data = {'form': form, 'titulo': "Actualizar Grupo Muscular"}
    return render(request, 'grupomuscular_update.html', data)

def Delete_Grupo_Muscular(request, id):

    try:
        grupo = GrupoMuscular.objects.get(id=id)
    except GrupoMuscular.DoesNotExist:
        return redirect('../Grupo_Muscular/')

    if request.method == 'POST':
        grupo.delete()
        return redirect('../Grupo_Muscular/')
    
    return render(request, 'grupomuscular_eliminar.html', {'grupo': grupo})

def Ejercicio(request):
    ejercicios = Ejercicio.objects.all()
    data = {'ejercicios': ejercicios}
    return render(request, 'ejercicios.html', data)

def Agregar_Ejercicio(request):

    form = EjerciciosForm()
    if request.method == 'POST':
        form = EjerciciosForm(request.POST)
        if form.is_valid():
            form.save()
        return Ejercicio(request)
    data = {
        'form': form,
        'titulo': 'Agregar Ejercicio'
    }
    return render(request, 'ejercicios_save.html', data)

def Actualizar_Ejercicio(request, id):

    ejercicio = Ejercicio.objects.get(id=id)
    form = EjerciciosForm(instance=ejercicio)
    if request.method == "POST":
        form = EjerciciosForm(request.POST, instance=ejercicio)
        if form.is_valid():
            form.save()
        return Ejercicio(request)
    data = {
        'form': form,
        'titulo': 'Actualizar Ejercicio'
    }
    return render(request, 'ejercicios_save.html', data)

def Delete_Ejercicio(request, id):

    try:
        ejercicio = Ejercicio.objects.get(id=id)
    except Ejercicio.DoesNotExist:
        return

@user_passes_test(lambda u: u.is_staff)
def GestionEjercicios(request):
    tipos_ejercicio = TipoEjercicio.objects.all()
    grupos_musculares = GrupoMuscular.objects.all()
    ejercicios = Ejercicio.objects.all()
    
    context = {
        'tipos_ejercicio': tipos_ejercicio,
        'grupos_musculares': grupos_musculares,
        'ejercicios': ejercicios
    }
    return render(request, 'gestion_ejercicios.html', context)

def vista_gestion_ejercicios(request):
    if request.method == 'POST':
        if 'tipo' in request.POST:
            TipoEjercicio.objects.create(
                nombre=request.POST['nombre']
            )
        elif 'region' in request.POST:
            GrupoMuscular.objects.create(
                nombre=request.POST['nombre'],
                region=request.POST['region']
            )
        else:
            ModeloEjercicio.objects.create(
                nombre=request.POST['nombre'],
                tipo_ejercicio_id=request.POST['tipo_ejercicio'],
                grupo_muscular_id=request.POST['grupo_muscular'],
                dificultad=request.POST['dificultad'],
                descripcion=request.POST.get('descripcion', '')
            )
        return redirect('gestion_ejercicios')

    context = {
        'tipos_ejercicio': TipoEjercicio.objects.all(),
        'grupos_musculares': GrupoMuscular.objects.all(),
        'ejercicios': ModeloEjercicio.objects.all(),
    }
    return render(request, 'gestion_ejercicios.html', context)

def ver_ejercicio(request, id):
    ejercicio = get_object_or_404(ModeloEjercicio, id=id)
    return JsonResponse({
        'nombre': ejercicio.nombre,
        'tipo': ejercicio.tipo_ejercicio.nombre,
        'grupo': ejercicio.grupo_muscular.nombre,
        'dificultad': ejercicio.dificultad,
        'descripcion': ejercicio.descripcion
    })

def editar_ejercicio(request, id):
    ejercicio = get_object_or_404(ModeloEjercicio, id=id)
    if request.method == 'POST':
        ejercicio.nombre = request.POST['nombre']
        ejercicio.tipo_ejercicio_id = request.POST['tipo_ejercicio']
        ejercicio.grupo_muscular_id = request.POST['grupo_muscular']
        ejercicio.dificultad = request.POST['dificultad']
        ejercicio.descripcion = request.POST.get('descripcion', '')
        ejercicio.save()
        return redirect('gestion_ejercicios')
    return JsonResponse({
        'id': ejercicio.id,
        'nombre': ejercicio.nombre,
        'tipo_ejercicio': ejercicio.tipo_ejercicio_id,
        'grupo_muscular': ejercicio.grupo_muscular_id,
        'dificultad': ejercicio.dificultad,
        'descripcion': ejercicio.descripcion
    })

def eliminar_ejercicio(request, id):
    if request.method == 'DELETE':
        ModeloEjercicio.objects.get(id=id).delete()
        return JsonResponse({'status': 'ok'})

def eliminar_tipo(request, id):
    if request.method == 'DELETE':
        TipoEjercicio.objects.get(id=id).delete()
        return JsonResponse({'status': 'ok'})

def eliminar_grupo(request, id):
    if request.method == 'DELETE':
        GrupoMuscular.objects.get(id=id).delete()
        return JsonResponse({'status': 'ok'})