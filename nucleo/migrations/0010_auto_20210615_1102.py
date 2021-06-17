# Generated by Django 3.1.7 on 2021-06-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0009_alumno_fechainicioexamen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='CorreoElectronico',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='Dni',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='FechaInicioExamen',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha inicio examen'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='FechaUltimoExamen',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha ultimo examen'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='NumeroLicencia',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]