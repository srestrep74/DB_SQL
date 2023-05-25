from django import forms
from django.contrib.auth.models import User
from .models import coleccionista
from .models import pieza, compra
from django import forms
from django.contrib.auth.forms import AuthenticationForm



class SignupForm(forms.ModelForm):
    class Meta:
        model = coleccionista
        fields = '__all__'


class LoginForm(AuthenticationForm):
    identificacion= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class piezaForm(forms.ModelForm):
    class Meta:
        model = pieza
        fields = '__all__'

class piezaFormUpdate(forms.ModelForm):
    class Meta:
        model = pieza
        fields = '__all__'

class buyForm(forms.ModelForm):
    class Meta:
        model = compra
        fields = '__all__'

class verColeccion(forms.Form):
    identificacion = forms.CharField()

class eliminarForm(forms.Form):
    pieza = forms.CharField()

class editPiece(forms.Form):
    id_pieza= forms.CharField()
    nombre = forms.CharField()
    valor_facial = forms.IntegerField()
    precio_avaluado = forms.IntegerField()
    ceca = forms.CharField()
    material = forms.CharField()
    peso = forms.IntegerField()
    diametro = forms.IntegerField()
    año = forms.IntegerField()
    tipo_articulo = forms.CharField()


        # Obtener la instancia del objeto a actualizar
        
        

