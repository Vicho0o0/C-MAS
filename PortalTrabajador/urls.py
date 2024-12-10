from django.urls import path, include
from PortalTrabajador import views

urlpatterns = [
    path('', views.IndexT),
    path('RegistroEntrada/', views.registro_entrada, name='registro_entrada'),
    path('Clases_profesor/', views.Clases_profesor),
    path('crear_clase/',views.Crear_Clase),
    path('ver_clase/<int:id>',views.Ver_Clase),
    path('actualizar_clase/<int:id>',views.Actualizar_Clase),
    path('eliminar_clase/<int:id>',views.Eliminar_Clase),
    path('registro_entrada/', views.RegistroEntrada, name='registro_entrada'),
    path('MembresiasAdmin/', views.MembresiasAdmin),
    path('crear_membresia/', views.CrearMembresias),
    path('eliminar_membresia/<int:id>', views.Eliminar_Membresia),
    path('actualizar_membresia/<int:id>',views.Actualizar_Membresia),
    path('Progreso_Trabajador/', views.Progreso_Trabajador, name='progreso_trabajador'),
    path('Tipo_Ejercicio/', views.Tipo_Ejercicio),
    path('crear_tipo_ejercicio/',views.Agregar_Tipo_Ejercicio),
    path('actualizar_tipo_ejercicio/<int:id>/', views.Actualizar_Tipo_Ejercicio, name='actualizar_tipo_ejercicio'),
    path('delete_tipo_ejercicio/<int:id>',views.Delete_Tipo_Ejercicio),
    path('crear_grupo_muscular/',views.Agregar_Grupo_Muscular),
    path('Ejercicios/', views.Ejercicio),
    path('crear_ejercicio/',views.Agregar_Ejercicio),
    path('actualizar_ejercicio/<int:id>/', views.Actualizar_Ejercicio, name='actualizar_ejercicio'),
    path('delete_ejercicio/<int:id>',views.Delete_Ejercicio),
    path('gestion_ejercicios/', views.GestionEjercicios, name='gestion_ejercicios'),
    path('actualizar_tipo_ejercicio/<int:id>/', views.Actualizar_Tipo_Ejercicio, name='actualizar_tipo_ejercicio'),
    path('actualizar_grupo_muscular/<int:id>/', views.Actualizar_Grupo_Muscular, name='actualizar_grupo_muscular'),
    path('actualizar_ejercicio/<int:id>/', views.Actualizar_Ejercicio, name='actualizar_ejercicio'),
    path('eliminar-tipo/<int:id>/', views.Delete_Tipo_Ejercicio, name='eliminar_tipo_ejercicio'),
    path('eliminar-grupo/<int:id>/', views.Delete_Grupo_Muscular, name='eliminar_grupo_muscular'),
    path('eliminar-ejercicio/<int:id>/', views.Delete_Ejercicio, name='eliminar_ejercicio'),
    path('ver-ejercicio/<int:id>/', views.ver_ejercicio, name='ver_ejercicio'),
    path('editar-ejercicio/<int:id>/', views.editar_ejercicio, name='editar_ejercicio'),
    path('eliminar-ejercicio/<int:id>/', views.eliminar_ejercicio, name='eliminar_ejercicio'),
    path('grupomuscular_update/<int:id>/', views.Actualizar_Grupo_Muscular, name='grupomuscular_update'),
    path('grupomuscular_delete/<int:id>/', views.Delete_Grupo_Muscular, name='grupomuscular_delete'),
]