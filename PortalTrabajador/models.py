from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.rut}"
    
class RegisterEntrada(models.Model):
    perfil = models.ForeignKey("PortalTrabajador.Pefil", on_delete=models.CASCADE, related_name='perfil_portal_trabajador')
    hora_entrada = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Entrada: {self.perfil.user.first_name}"
