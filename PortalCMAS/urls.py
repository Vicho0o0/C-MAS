from django.urls import path
from django.contrib.auth.views import LogoutView
from PortalCMAS import views

urlpatterns = [
    path('', views.IndexC, name='indexC'),
    path('Membresias/', views.MembresiasUsuarios),
    path('PortalLogin/', views.Login),
    path('PortalRegistro/', views.Registro, name="PortalRegistro"),
    path('PortalAdmin/', views.Login_Admin, name='login_admin'),
    path('Clases_cliente/', views.Clases_cliente),
    path('Inscripcion/', views.Inscripcion),
    path('progreso/', views.ProgresoCliente, name='progreso'),
    path('graficos_cliente/', views.GraficoCliente, name='grafico_cliente'),
    path('graficos_cliente/get_chart/', views.get_chart, name='get_chart'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]