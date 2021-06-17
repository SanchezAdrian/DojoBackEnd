from django.db import models
from rest_framework import serializers
from nucleo.models import HistorialExamenes, OnlineParts, Parte, ParteExamen, Tutor, User, Alumno


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
    def update(self, instance, validated_data):
        updated_user= super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class TutorModelSerializar(serializers.ModelSerializer):
    user = UserSerializers()
    class Meta:
        model = Tutor
        fields = ('id','Nombre','Apellidos','user')


class VideosSerialzier(serializers.ModelSerializer):
    class Meta:
        model = OnlineParts
        fields = ('Url','Kyu','Nombre','Descripcion','PermitidosExtra')
   

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id','Nombre','Apellidos','Direccion','FechaNacimiento','Telefono','Clase','Activado','Horario','FechaUltimoExamen','FechaInicioExamen','tur','kyu','examenActivo','Dni','NumeroLicencia','CorreoElectronico')

    # def create(self, validate_data):
    #     userInstance = User.objects.get(validate_data)
    #     instance = Perfil.objects.create(**validate_data,User=userInstance)
    #     return instance

class HistorialSerializer(serializers.ModelSerializer):
    Alumno = AlumnoSerializer()
    class Meta:
        model = HistorialExamenes
        fields = ['id','Alumno','Fecha','Kyu']

class ParteExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParteExamen
        fields = ('id','Part','Realizadas','Nota','Finalizada','Alum','Info')

class ParteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parte
        fields = ('Categoria','Orientacion','Nombre','id')