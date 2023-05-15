from django.db import models
from django.core import validators
# Create your models here.
class pieza(models.Model):
    id_pieza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    valor_facial = models.CharField(max_length=45)
    precio_avaluado = models.IntegerField()
    ceca = models.CharField(max_length=45)
    material = models.CharField(max_length=45)
    peso = models.FloatField()
    diametro = models.FloatField()
    año = models.IntegerField(
        validators=[
        validators.MinValueValidator(1900),
        validators.MaxValueValidator(2100)
        ]
    )
    tipo_art_options = (('Moneda','Moneda') , ('Billete', 'Billete'))
    tipo_articulo = models.CharField(max_length=45, choices=tipo_art_options)
