from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Schedule(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut_usuario = models.CharField(max_length=12, unique=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    plan = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True)
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut}) {self.email}"
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

class RegistroEntrada(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True, blank=True)
    hora_entrada = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Entrada: {self.perfil.user.first_name} {self.perfil.user.last_name} ({self.hora_entrada})"

class MetricasCliente(models.Model):
    rut_cliente = models.CharField(max_length=12, unique=True)
    altura = models.IntegerField(null=True)
    peso = models.IntegerField(null=True)
    horas_entrenadas = models.IntegerField(null=True)
    fecha_marca = models.DateTimeField(auto_now_add=True)

class TipoEjercicio(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipoejercicio'
        verbose_name = 'TipoEjercicio'
        verbose_name_plural = 'TipoEjercicios'
        ordering = ['id']

class GrupoMuscular(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'grupomuscular'
        verbose_name = 'GrupoMuscular'
        verbose_name_plural = 'GruposMusculares'
        ordering = ['id']

class Ejercicios(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    tipo_ejercicio = models.ForeignKey(TipoEjercicio, on_delete=models.CASCADE)
    grupo_muscular = models.ForeignKey(GrupoMuscular, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'ejercicios'
        verbose_name = 'Ejercicios'
        verbose_name_plural = 'Ejercicios'
        ordering = ['id']

class MetricasEjerciciosCliente(models.Model):
    rut_cliente = models.CharField(max_length=12, unique=True)
    nombre = models.ForeignKey(Ejercicios, on_delete=models.CASCADE)
    peso = models.IntegerField(null=True)
    repeticiones = models.IntegerField(null=True)
    fecha_marca = models.DateTimeField(auto_now_add=True)

class Clases(models.Model):
    Horario = models.CharField(max_length=50)
    Actividad = models.CharField(max_length=50)
    Maquinas_Diponibles = models.CharField(max_length=50)

class Membresias(models.Model):
    Nombre = models.CharField(max_length=30)
    Precio = models.IntegerField(default=0)
    Horario1 = models.CharField(max_length=50)
    Horario2 = models.CharField(max_length=50)

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.perfil.save()