# Generated by Django 5.1.1 on 2024-09-16 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0003_alter_prestamo_biblioteca_material_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='Nro_Documento',
            field=models.CharField(max_length=40, verbose_name='nro_documento'),
        ),
    ]
