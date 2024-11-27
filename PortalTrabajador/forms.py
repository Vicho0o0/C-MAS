from django import forms
from PortalCMAS.models import TipoEjercicio, GrupoMuscular, MetricasEjerciciosCliente, MetricasCliente 

class RegistroEntradaForm(forms.Form):
    rut = forms.CharField(
        max_length=12,
        label="RUT",
        widget=forms.TextInput(attrs={'placeholder': 'Ej: 12345678-9'})
    )

