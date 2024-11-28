from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from PortalCMAS.models import * 

class RegistroEntradaForm(forms.Form):
    rut_usuario = forms.CharField(
        max_length=12,
        label="RUT",
        widget=forms.TextInput(attrs={'placeholder': 'Ej: 12345678-9'})
    )

class MetricasClienteForm(forms.ModelForm):
    class Meta:
        model = MetricasCliente
        fields = [
            'rut_cliente',
            'peso',
            'horas_entrenadas',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rut_cliente'].widget.attrs['readonly'] = True

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
        ]


class MetricasEjerciciosClienteForm(forms.ModelForm):
    class Meta:
        model = MetricasEjerciciosCliente
        fields = [
            'rut_cliente',
            'nombre',
            'peso',
            'repeticiones',
            'series',
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