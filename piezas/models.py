from django.db import models
from django.core import validators
from enum import Enum
from django.utils import timezone
# Create your models here.

class enum_Tipo_Cuenta(Enum):
    OPCION1 = 'Corriente'
    OPCION2 = 'Ahorros'

class estado_conservacion(Enum):
    OPCION1 = 'Mala'
    OPCION2 = 'Buena'
    OPCION3 = 'Regular'
    OPCION4 = 'Excelente'


class coleccionista(models.Model):
    identificacion = models.CharField(primary_key=True, max_length=45)
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=64)
    fecha_registro = models.DateField(default= timezone.now)
    numero_tarjeta_bancaria = models.CharField(max_length=45)
    tipo_cuenta =  models.CharField(max_length=45)




class pieza(models.Model):
    id_pieza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    valor_facial = models.CharField(max_length=45)
    precio_avaluado = models.IntegerField()
    coleccionista= models.ForeignKey(coleccionista, on_delete=models.CASCADE)
    ceca = models.CharField(max_length=45,null=True)
    material = models.CharField(max_length=45,null=True)
    peso = models.FloatField()
    diametro = models.FloatField(null=True)
    año = models.IntegerField(
        validators=[
        validators.MinValueValidator(1000),
        validators.MaxValueValidator(2100)
        ]
    )
    tipo_art_options = (('Moneda','Moneda') , ('Billete', 'Billete'))
    tipo_articulo = models.CharField(max_length=45, choices=tipo_art_options)

class compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha_venta = models.DateField(default=timezone.now)
    valor_compra = models.IntegerField()
    id_coleccionista = models.CharField(max_length=45)
    id_vendedor = models.CharField(max_length=45 )   
    id_pieza = models.IntegerField()

