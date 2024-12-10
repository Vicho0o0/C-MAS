from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from PortalCMAS.models import * 

class RegistroEntradaForm(forms.Form):
    rut = forms.CharField(
        max_length=12,
        label="RUT",
        widget=forms.TextInput(attrs={'placeholder': 'Ej: 12345678-9'})
    )

class MetricasClienteForm(forms.ModelForm):
    class Meta:
        model = MetricasCliente
        fields = ['altura', 'peso', 'horas_entrenadas']
        widgets = {
            'altura': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Altura en cm'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso en kg'}),
            'horas_entrenadas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Horas entrenadas'})
        }

class AgregarTipoEjercicioForm(forms.ModelForm):
    class Meta:
        model = TipoEjercicio
        fields = [
            'nombre',
        ]

class AgregarGrupoMuscularForm(forms.ModelForm):
    class Meta:
        model = GrupoMuscular
        fields = [
            'nombre',
        ]

class EjerciciosForm(forms.ModelForm):
    class Meta:
        model = Ejercicios
        fields = [
            'nombre',
            'tipo_ejercicio',
            'grupo_muscular',
            'dificultad',
            'descripcion'
        ]


class MetricasEjerciciosClienteForm(forms.ModelForm):
    class Meta:
        model = MetricasEjerciciosCliente
        fields = ['nombre', 'peso', 'repeticiones']
        widgets = {
            'nombre': forms.Select(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso en kg'}),
            'repeticiones': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de repeticiones'})
        }

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

class GrupoMuscularForm(forms.ModelForm):
    class Meta:
        model = GrupoMuscular
        fields = ['nombre', 'region']