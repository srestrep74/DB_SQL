from django.db import models
from django.core import validators
from enum import Enum
# Create your models here.

class enum_Tipo_Cuenta(Enum):
    OPCION1 = 'Corriente'
    OPCION2 = 'Ahorros'

class estado_conservacion(Enum):
    OPCION1 = 'Mala'
    OPCION2 = 'Buena'
    OPCION3 = 'Regular'
    OPCION4 = 'Excelente'


class departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=45)

class ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=45)
    id_departamento = models.ForeignKey(departamento, on_delete=models.CASCADE)

class direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    id_ciudad = models.ForeignKey(ciudad, on_delete=models.CASCADE)
    codigo_postal = models.CharField(max_length=30, null=True)
    celular = models.CharField(max_length=20)
    direccion = models.CharField(max_length=45)

class coleccionista(models.Model):
    identifiacion = models.CharField(max_length=45, primary_key=True)
    primer_nombre = models.CharField(max_length=45)
    segundo_nombre = models.CharField(max_length=45, null=True)
    primer_apellido = models.CharField(max_length=45)
    segundo_apellido = models.CharField(max_length=45, null=True)
    id_direccion = models.ForeignKey(direccion, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=64)
    fecha_registro = models.DateField()
    numero_tarjeta_bancaria = models.CharField(max_length=45)
    tipo_cuenta = models.CharField(max_length=45, choices=[(choice.name, choice.value) for choice in enum_Tipo_Cuenta])

class coleccion(models.Model):
    id_coleccion = models.AutoField(primary_key=True)
    cant_piezas = models.IntegerField()
    fecha_inicio_coleccion = models.DateField()
    estado_conservacion = models.CharField(max_length=45, choices = [(choice.name, choice.value) for choice in estado_conservacion], null=True)
    identificacion_coleccionista = models.ForeignKey(coleccionista, on_delete=models.CASCADE, unique=True)


class pieza(models.Model):
    id_pieza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    valor_facial = models.CharField(max_length=45)
    precio_avaluado = models.IntegerField()
    ceca = models.CharField(max_length=45,null=True)
    material = models.CharField(max_length=45,null=True)
    peso = models.FloatField()
    diametro = models.FloatField(null=True)
    año = models.IntegerField(
        validators=[
        validators.MinValueValidator(1900),
        validators.MaxValueValidator(2100)
        ]
    )
    id_coleccion = models.ForeignKey(coleccion,default=1, on_delete=models.CASCADE)
    tipo_art_options = (('Moneda','Moneda') , ('Billete', 'Billete'))
    tipo_articulo = models.CharField(max_length=45, choices=tipo_art_options)

class compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha_venta = models.DateField()
    valor_compra = models.IntegerField()
    id_coleccionista = models.CharField(max_length=45)
    id_vendedor = models.CharField(max_length=45 )   
    id_pieza = models.ForeignKey(pieza, on_delete=models.CASCADE)
