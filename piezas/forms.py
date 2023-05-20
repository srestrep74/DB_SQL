from django import forms
from .models import pieza

class pieza(forms.ModelForm):
    class Meta:
        model = pieza
        fields = '__all__'