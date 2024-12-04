from django import forms
from PortalCMAS.models import TipoEjercicio, GrupoMuscular, MetricasEjerciciosCliente, MetricasCliente 

class RegistroEntradaForm(forms.Form):
    rut = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 12345678-9',
            'oninput': 'formatRut(this)',
            'required': True
        })
    )
class GrupoMuscularForm(forms.ModelForm):
    class Meta:
        model = GrupoMuscular
        fields = ['nombre', 'region']
