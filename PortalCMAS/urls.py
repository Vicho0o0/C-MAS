from django.urls import path, include
from PortalCMAS import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.IndexC, name='indexC'),
    path('Membresias/', views.MembresiasUsuarios),
    path('PortalLogin/', views.Login),
    path('PortalRegistro/', views.Registro, name="PortalRegistro"),
    path('PortalAdmin/', views.Login_Admin, name='login_admin'),
    path('Clases_cliente/', views.Clases_cliente),
    path('Inscripcion/', views.Inscripcion),
    path('progreso/', views.ProgresoCliente),
    path('graficos_cliente/', views.GraficoCliente, name='grafico_cliente'),
    path('graficos_cliente/get_chart/', views.get_chart, name='get_chart'),
    path('metricas_cliente/', views.Metricas_Cliente),
    path('metricas_entreno/', views.Metricas_Entreno),
]