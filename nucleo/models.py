from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tutor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    Nombre=models.CharField(max_length=30,null=True)
    Apellidos=models.CharField(max_length=70,null=True)

    def __str__(self):
        return self.Nombre+" "+self.Apellidos
    

class Parte(models.Model):
    
    GONOSEN = 1
    GOSHIN = 2 
    AGARRESFUNDAMENTALES = 3 
    KATAS = 4
    KIHON = 5
    TEORIA = 6
    GOLPES = 7
    CAIDAS = 8 
    GUARDIAS = 9
    EXTRA = 10
    CAT_CHOICES = (
        (GONOSEN, 'Go-no-sen'),
        (GOSHIN, 'Go-shin'),
        (AGARRESFUNDAMENTALES, 'Agarres fundamentales'),
        (KATAS, 'Katas'),
        (KIHON, 'Kihon'),
        (TEORIA, 'Teoria'),
        (GOLPES, 'golpes'),
        (CAIDAS, 'Caidas'),
        (GUARDIAS, 'Guardias'),
        (EXTRA, 'Extra'),
    )

    FRONTAL = 1
    LATERAL = 2 
    ATRAS = 3 
    NADA = 4
    SUELO = 5
    OR_CHOICES = (
        (FRONTAL, 'Frontal'),
        (LATERAL, 'Lateral'),
        (ATRAS, 'Atras'),
        (NADA, ''),
        (SUELO, 'Suelo'),
       
    )

    Categoria=models.PositiveSmallIntegerField(choices=CAT_CHOICES,default=1,null=True, blank=True)
    Orientacion=models.PositiveSmallIntegerField(choices=OR_CHOICES,default=4,null=True, blank=True)
    Nombre=models.CharField(max_length=120,null=True)

    def __str__(self):
        return self.CAT_CHOICES[self.Categoria-1][1]+" "+self.Nombre+" "+ self.OR_CHOICES[self.Orientacion-1][1]

class Alumno(models.Model):
    
    Nombre=models.CharField(max_length=30,null=True)
    Apellidos=models.CharField(max_length=70,null=True)
    Direccion=models.CharField(max_length=50,null=True)
    Telefono=models.CharField(max_length=9,null=True)
    FechaNacimiento=models.DateField(null=True, verbose_name="Fecha nacimiento")
    Activado=models.BooleanField(default="True")
    Clase=models.CharField(max_length=9,null=True)
    Horario=models.CharField(max_length=20,null=True)
    FechaUltimoExamen=models.DateField(null=True,blank=True, verbose_name="Fecha ultimo examen")
    FechaInicioExamen=models.DateField(null=True,blank=True, verbose_name="Fecha inicio examen")
    tur=models.ForeignKey(Tutor, on_delete=models.CASCADE)
    kyu=models.CharField(max_length=9,null=True)
    examenActivo=models.BooleanField(default=False)
    Dni=models.CharField(max_length=9,null=True,blank=True)
    NumeroLicencia=models.CharField(max_length=20,null=True,blank=True)
    CorreoElectronico=models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):
        return self.Nombre + self.kyu +str(self.FechaUltimoExamen) + str(self.examenActivo)

class HistorialExamenes(models.Model):
    Alumno=models.ForeignKey('Alumno',on_delete=models.CASCADE, blank=True)
    Fecha=models.DateField(null=True, verbose_name="Fecha finalización examen")
    Kyu=models.CharField(max_length=9,null=True)

    def __str__(self):
        return self.Alumno.Nombre + self.Kyu

class ParteExamen(models.Model):
    Part=models.ForeignKey(Parte,on_delete=models.CASCADE)
    Realizadas=models.IntegerField(null=True)
    Necesarias=models.IntegerField(default=1)
    Nota=models.CharField(max_length=2,null=True)
    Finalizada=models.BooleanField(default="False")
    Alum=models.ForeignKey('Alumno',on_delete=models.CASCADE, blank=True)
    Info=models.TextField(null=True)

    def __str__(self):
        return self.Alum.Nombre+" "+self.Part.Nombre

class OnlineParts(models.Model):
    Url=models.CharField(max_length=600,null=True)
    Kyu=models.CharField(max_length=9,null=True)
    Nombre=models.CharField(max_length=90,null=True)
    Descripcion=models.CharField(max_length=500,null=True)
    PermitidosExtra=models.ManyToManyField(Alumno)

    def __str__(self):
        return self.Nombre