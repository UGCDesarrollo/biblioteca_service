# Generated by Django 5.1.1 on 2024-09-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0002_userapikey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='Biblioteca_material',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='Nro_Documento',
            field=models.CharField(max_length=40),
        ),
    ]
