# Generated by Django 3.1.4 on 2021-04-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0002_auto_20210419_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='PermisoExtra',
        ),
        migrations.AddField(
            model_name='onlineparts',
            name='PermitidosExtra',
            field=models.ManyToManyField(to='nucleo.Alumno'),
        ),
    ]