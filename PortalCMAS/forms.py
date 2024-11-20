from django import forms
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
    nombre = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu nombre',
            'required' : 'true'
        })
    )
    password= forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Ingresa tu contraseña',
            'required' : 'true'   
        })
    )
    
class FormRegistro(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        label="Contraseña"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirmar Contraseña'}),
        label="Confirmar Contraseña"
    )

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'rut' ,'password'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password = cleaned_data.get("password")

        if password and password and password != password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password = self.cleaned_data["password"]
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