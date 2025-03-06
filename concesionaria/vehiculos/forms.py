from django import forms
from .models import Vehiculo, Comentario, VehiculoImage

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'cant_puertas', 'cilindrada', 'combustible', 'pais_fabricacion', 'precio_en_dolares']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control custom-class', 'rows': 4}),
        }

class VehiculoImageForm(forms.ModelForm):
    class Meta:
        model = VehiculoImage
        fields = [
            'vehiculo', 
            'image',]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control  custom-class'}),
        }

