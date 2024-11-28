from django.contrib import admin
from PortalCMAS.models import *

# Register your models here.

class TipoEjercicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ['nombre']
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(TipoEjercicio, TipoEjercicioAdmin)

class GrupoMuscularAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ['nombre']
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(GrupoMuscular, GrupoMuscularAdmin)

class EjerciciosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_ejercicio', 'grupo_muscular')
    search_fields = ['nombre']
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Ejercicios, EjerciciosAdmin)

class MetricasClienteAdmin(admin.ModelAdmin):
    list_display = ('rut_cliente', 'peso','horas_entrenadas')
    search_fields = ['rut_cliente']
    readonly_fields = ('rut_cliente','fecha_marca',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(MetricasCliente, MetricasClienteAdmin)

class MetricasEjerciciosClienteAdmin(admin.ModelAdmin):
    list_display = ('rut_cliente', 'nombre', 'peso', 'repeticiones', 'series')
    search_fields = ['rut_cliente']
    readonly_fields = ('fecha_marca',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(MetricasEjerciciosCliente, MetricasEjerciciosClienteAdmin)
