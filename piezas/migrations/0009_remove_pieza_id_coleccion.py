# Generated by Django 4.1.9 on 2023-05-29 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piezas', '0008_alter_pieza_año'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pieza',
            name='id_coleccion',
        ),
    ]