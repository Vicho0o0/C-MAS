from django.urls import path, include
from PortalCMAS import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Portal_Trabajador/', include('PortalTrabajador.urls')),
    path('', include('PortalCMAS.urls')),
    path('Comunidad/', views.Comunidad),
    path('Contactos/', views.Contactos),
]
