from django.urls import path
from PortalCMAS.views import Index, MembresiasUsuarios, Login, Registro, Clases_cliente, Clases_profesor, Comunidad, Contactos, Inscripcion, RegistroEntrada, Metricas_clientes, Login_Admin, Crear_Clase, Ver_Clase, Actualizar_Clase, Eliminar_Clase, MembresiasAdmin, CrearMembresias, Eliminar_Membresia, Actualizar_Membresia

urlpatterns = [
    path('', Index),
    path('Membresias/', MembresiasUsuarios),
    path('PortalLogin/', Login),
    path('PortalRegistro/', Registro, name="PortalRegistro"),
    path('Clases_cliente/', Clases_cliente),
    path('Clases_profesor/', Clases_profesor),
    path('crear_clase/',Crear_Clase),
    path('ver_clase/<int:id>',Ver_Clase),
    path('actualizar_clase/<int:id>',Actualizar_Clase),
    path('eliminar_clase/<int:id>',Eliminar_Clase),
    path('Progreso/', Metricas_clientes),
    path('Comunidad/', Comunidad),
    path('Contactos/', Contactos),
    path('Inscripcion/', Inscripcion),
    path('RegistroEntrada/', RegistroEntrada),
    path('PortalAdmin/', Login_Admin),
    path('MembresiasAdmin/', MembresiasAdmin),
    path('crear_membresia/', CrearMembresias),
    path('eliminar_membresia/<int:id>', Eliminar_Membresia),
    path('actualizar_membresia/<int:id>',Actualizar_Membresia),
]
