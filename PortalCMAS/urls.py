from django.urls import path
from PortalCMAS import views
urlpatterns = [
    path('', views.GraficoCliente, name='grafico_cliente'),
    path('get_chart/', views.get_chart, name='get_chart'),
]