from django.contrib import admin
from PortalCMAS.models import MetricasEjerciciosCliente, TipoEjercicio, GrupoMuscular, Ejercicios

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
