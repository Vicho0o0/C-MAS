from django.db import models

# Create your models here.

class TipoEjercicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre

class GrupoMuscular(models.Model):
    REGIONES = [
        ('superior', 'Superior'),
        ('inferior', 'Inferior'),
    ]
    nombre = models.CharField(max_length=100)
    region = models.CharField(max_length=20, choices=REGIONES)
    
    def __str__(self):
        return self.nombre

class Ejercicio(models.Model):
    DIFICULTADES = [
        ('principiante', 'Principiante'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoEjercicio, on_delete=models.CASCADE)
    grupo_muscular = models.ForeignKey(GrupoMuscular, on_delete=models.CASCADE)
    dificultad = models.CharField(max_length=20, choices=DIFICULTADES)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre
