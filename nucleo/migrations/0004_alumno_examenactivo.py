# Generated by Django 3.1.7 on 2021-06-04 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0003_auto_20210419_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='examenActivo',
            field=models.BooleanField(default=False),
        ),
    ]
