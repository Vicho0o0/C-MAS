from django.urls import path
from PortalCMAS import views
urlpatterns = [
    path('', views.IndexC),
    path('Membresias/', views.MembresiasUsuarios),
    path('PortalLogin/', views.Login),
    path('PortalRegistro/', views.Registro, name="PortalRegistro"),
    path('Clases_cliente/', views.Clases_cliente),
    path('Inscripcion/', views.Inscripcion),
    path('progreso/', views.ProgresoCliente),
    path('graficos_cliente/', views.GraficoCliente, name='grafico_cliente'),
    path('graficos_cliente/get_chart/', views.get_chart, name='get_chart'),
]