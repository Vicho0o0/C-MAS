from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RegistroEntrada, Metricas, Clases, Membresias, Cliente

class RegistroEntradaForm(forms.Form):
    rut = forms.CharField(
        max_length=12,
        label="RUT",
        widget=forms.TextInput(attrs={'placeholder': 'Ej: 12345678-9'})
    )

class MetricasForm(forms.ModelForm):
    class Meta:
        model = Metricas
        fields = [
            'altura', 
            'peso', 
            'peso_press_banca', 
            'peso_press_inclinado', 
            'peso_fondos', 
            'peso_jalon_al_pecho', 
            'peso_remo_polea', 
            'peso_remo_libre',
            'peso_dominada',
            'peso_sentadilla_libre',
            'peso_sentadilla_bulgara',
            'peso_maquina_cuadriceps',
            'peso_maquina_isquiotibiales',
            'peso_gemelos',
            'peso_biceps_mancuerna',
            'peso_triceps_mancuerna',
            'peso_elevaciones_laterales',
            'peso_elevaciones_laterales_posterior',
            'peso_press_militar',
        ]

class ClasesForm(forms.ModelForm):
    class Meta:
        model = Clases
        fields = [
            'Horario', 
            'Actividad', 
            'Maquinas_Diponibles',
        ]
                
class FormLogin(forms.Form):
    rut = forms.CharField(
        label="RUT",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 12345678-9',
            'required': 'true'
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu contraseña',
            'required': 'true'   
        })
    )
    
class FormRegistro(UserCreationForm):
    rut = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 12345678-9',
            'oninput': 'formatRut(this)'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'rut', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
 
class MembresiasForm(forms.ModelForm):
    class Meta:
        model=Membresias
        fields= [
            'Nombre',
            'Precio',
            'Horario1',
            'Horario2',
        ]