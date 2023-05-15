from django import forms
from .models import pieza

class pieza (forms.ModelForm):
    class Meta:
        model = pieza
        fields = '__all__'
        widgets = {
            'tipo_articulo' : forms.Select(choices=pieza.tipo_art_options)
        }