from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth import *
from django.contrib import messages
from django.conf import settings
from .models import Schedule, Cliente, RegistroEntrada
from PortalCMAS.models import Clases, Membresias
from .forms import RegistroEntradaForm, MetricasForm, ClasesForm, FormLogin, MembresiasForm, FormRegistro

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
    form = FormLogin(request.POST or None)
    if request.method == "POST" and form.is_valid():
        nombre = form.cleaned_data['nombre']
        password = form.cleaned_data['password']
        user = authenticate(request, nombre=nombre, password=password)
        if user is not None:
            login(request, user)
            return redirect('../index')
        else:
            messages.error(request,"Nombre o Contraseña incorrectos.")
    return render(request, 'PortalLogin.html', {'form': form})

def Registro(request):
    if request.method == "POST":
        form = FormRegistro(request.POST)
        if form.is_valid():
            # Crear el usuario sin guardarlo aún
            user = form.save(commit=False)

            # Establecer la contraseña en formato hash
            password = form.cleaned_data.get("password")
            if password:
                # Encriptar la contraseña
                user.password = make_password(password)
            # Guardar el usuario en la base de datos
            user.save()

            # Enviar mensaje de éxito
            messages.success(request, "Registro Exitoso. Puedes logear ahora.")
            return redirect('../PortalLogin')
        else:
            # Mostrar errores si el formulario no es válido
            messages.error(request, "Corrige los campos señalados por favor")
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

def Metricas_clientes(request):
    form=MetricasForm()
    if request.method=='POST':
        form=MetricasForm(request.POST)
        if form.is_valid():
            form.save()
        return Index(request)
    data={'form':form,'titulo':'Agregar Medidas'}
    return render(request,'Metricas.html',data)


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