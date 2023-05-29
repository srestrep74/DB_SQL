# Generated by Django 4.1.9 on 2023-05-28 00:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('piezas', '0006_delete_coleccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coleccionista',
            name='fecha_registro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fecha_venta',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
