from django.urls import path, include
from PortalTrabajador import views

urlpatterns = [
    path('', views.IndexT),
    path('Clases_profesor/', views.Clases_profesor),
    path('crear_clase/',views.Crear_Clase),
    path('ver_clase/<int:id>',views.Ver_Clase),
    path('actualizar_clase/<int:id>',views.Actualizar_Clase),
    path('eliminar_clase/<int:id>',views.Eliminar_Clase),
    path('registro-entrada/', views.RegistroEntrada, name='registro_entrada'),
    path('MembresiasAdmin/', views.MembresiasAdmin),
    path('crear_membresia/', views.CrearMembresias),
    path('eliminar_membresia/<int:id>', views.Eliminar_Membresia),
    path('actualizar_membresia/<int:id>',views.Actualizar_Membresia),
    path('Tipo_Ejercicio/', views.Tipo_Ejercicio),
    path('crear_tipo_ejercicio/',views.Agregar_Tipo_Ejercicio),
    path('actualizar_tipo_ejercicio/<int:id>',views.Actualizar_Tipo_Ejercicio),
    path('delete_tipo_ejercicio/<int:id>',views.Delete_Tipo_Ejercicio),
]