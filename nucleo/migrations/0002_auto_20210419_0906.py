# Generated by Django 3.1.4 on 2021-04-19 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='PermisoExtra',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='parte',
            name='Orientacion',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Frontal'), (2, 'Lateral'), (3, 'Atras'), (4, ''), (5, 'Suelo')], default=4, null=True),
        ),
    ]