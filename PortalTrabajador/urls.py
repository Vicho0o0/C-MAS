from django.urls import path, include
from PortalTrabajador import views

urlpatterns = [
    path('', views.IndexT),
    path('Clases_profesor/', views.Clases_profesor),
    path('crear_clase/',views.Crear_Clase),
    path('ver_clase/<int:id>',views.Ver_Clase),
    path('actualizar_clase/<int:id>',views.Actualizar_Clase),
    path('eliminar_clase/<int:id>',views.Eliminar_Clase),
    path('registro-entrada/', views.Registro_Entrada, name='registro_entrada'),
    path('MembresiasAdmin/', views.MembresiasAdmin),
    path('crear_membresia/', views.CrearMembresias),
    path('eliminar_membresia/<int:id>', views.Eliminar_Membresia),
    path('actualizar_membresia/<int:id>',views.Actualizar_Membresia),
    path('Progreso_Trabajador/', views.Progreso_Trabajador),
    path('Tipo_Ejercicio/', views.Tipo_Ejercicio),
    path('crear_tipo_ejercicio/',views.Agregar_Tipo_Ejercicio),
    path('actualizar_tipo_ejercicio/<int:id>',views.Actualizar_Tipo_Ejercicio),
    path('delete_tipo_ejercicio/<int:id>',views.Delete_Tipo_Ejercicio),
    path('Grupo_Muscular/', views.Grupo_Muscular),
    path('crear_grupo_muscular/',views.Agregar_Grupo_Muscular),
    path('actualizar_grupo_muscular/<int:id>',views.Actualizar_Grupo_Muscular),
    path('delete_grupo_muscular/<int:id>',views.Delete_Grupo_Muscular),
    path('Ejercicios/', views.Ejercicio),
    path('crear_ejercicio/',views.Agregar_Ejercicio),
    path('actualizar_ejercicio/<int:id>',views.Actualizar_Ejercicio),
    path('delete_ejercicio/<int:id>',views.Delete_Ejercicio),
]