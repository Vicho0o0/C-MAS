from django.db import models

class Schedule(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    plan = models.CharField(max_length=100)
    password = models.CharField(max_length=100, blank=True)
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut}) {self.email}"
    
class RegistroEntrada(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    hora_entrada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entrada: {self.cliente.nombre} ({self.hora_entrada})"

class Metricas(models.Model):
    altura = models.IntegerField(null=True)
    peso = models.IntegerField(null=True)
    peso_press_banca = models.IntegerField(null=True)
    peso_press_inclinado = models.IntegerField(null=True)
    peso_fondos = models.IntegerField(null=True)
    peso_jalon_al_pecho = models.IntegerField(null=True)
    peso_remo_polea = models.IntegerField(null=True)
    peso_remo_libre = models.IntegerField(null=True)
    peso_dominada = models.IntegerField(null=True)
    peso_sentadilla_libre = models.IntegerField(null=True)
    peso_sentadilla_bulgara = models.IntegerField(null=True)
    peso_maquina_cuadriceps = models.IntegerField(null=True)
    peso_maquina_isquiotibiales = models.IntegerField(null=True)
    peso_gemelos = models.IntegerField(null=True)
    peso_biceps_mancuerna = models.IntegerField(null=True)
    peso_triceps_mancuerna = models.IntegerField(null=True)
    peso_elevaciones_laterales = models.IntegerField(null=True)
    peso_elevaciones_laterales_posterior = models.IntegerField(null=True)
    peso_press_militar = models.IntegerField(null=True)

class Clases(models.Model):
    Horario = models.CharField(max_length=50)
    Actividad = models.CharField(max_length=50)
    Maquinas_Diponibles = models.CharField(max_length=50)

class Membresias(models.Model):
    Nombre = models.CharField(max_length=30)
    Precio = models.IntegerField(default=0)
    Horario1 = models.CharField(max_length=50)
    Horario2 = models.CharField(max_length=50)