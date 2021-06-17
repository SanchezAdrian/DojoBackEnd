from decimal import Context
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from nucleo.models import ParteExamen, Alumno, Parte
from nucleo.forms import *
# from dateutil.relativedelta import relativedelta # uso de relativedata para obtener la edad facilmente
from rest_framework.views import APIView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.views.generic.detail import DetailView
from datetime import datetime
# from rest_framework.authtoken.models import Token
# Create your views here.
from nucleo.serializer import AlumnoSerializer, HistorialSerializer, ParteExamenSerializer, ParteSerializer, TutorModelSerializar, VideosSerialzier, UserSerializers
from django.db.models.functions import Length
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import RetrieveAPIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


import django.contrib.auth.password_validation as validators

class VistaCrearExamen(CreateView):
    model = ParteExamen
    form_class=CreacionExamenForm
    template_name = 'CreateExam.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context

class VistaAsignarExamen(CreateView):
    model = ParteExamen
    form_class=CreacionExamenForm
    template_name = 'AsignarExam.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        alumnos = Alumno.objects.all()
        context['alumnos_list']= alumnos
        return context


class AsignacionExamen(ListView): 
    model = ParteExamen 
    template_name = 'Asignacion.html'
    success_url = '/'
    kyu=0
        
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if(self.kwargs['pk'] is not None):
            alumno = Alumno.objects.get(id = self.kwargs['pk'])
            cinturon = Alumno.objects.get(Nombre=alumno.kyu)
            if (alumno.kyu=="B" or alumno.kyu=="BA"): 
                kyu=1
            elif (alumno.kyu=="A" or alumno.kyu=="AN"): 
                kyu=2
            elif (alumno.kyu=="N" or alumno.kyu=="NV"): 
                kyu=3
            elif (alumno.kyu=="V" or alumno.kyu=="VA"): 
                kyu=4
            elif (alumno.kyu=="AZ" or alumno.kyu=="AM"): 
                kyu=5
            partes = ParteExamen.objects.filter(Alum=cinturon)
            for i in range(kyu):
                if (i == 1 ): 
                    cinturon = Alumno.objects.get(Nombre="B")
                elif (i == 2): 
                    cinturon = Alumno.objects.get(Nombre="A")
                elif (i == 3): 
                    cinturon = Alumno.objects.get(Nombre="N")
                elif (i == 4): 
                    cinturon = Alumno.objects.get(Nombre="V")
                elif (i == 2): 
                    cinturon = Alumno.objects.get(Nombre="AZ")
                partes = ParteExamen.objects.filter(Alum=cinturon)
                for x in partes:
                    x.Alum=alumno
                    x.pk=None
                    x.save()
            partes2=ParteExamen.objects.filter(Alum=alumno)
            context['partes_list']=partes2
        return context

class VerExamen(ListView): 
    model = ParteExamen 
    template_name = 'VerExamen.html'
    success_url = '/'
        
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if(self.kwargs['pk'] is not None):
            alumno = Alumno.objects.get(id = self.kwargs['pk'])
            partes=ParteExamen.objects.filter(Alum=alumno)
            context['partes_list']=partes
            context['pendientes']=partes.filter(Finalizada=False)
            context['realizadas']=partes.filter(Finalizada=True)
        return 
        

        ### API

class AsginacionExamen_API(RetrieveAPIView):
     permission_classes = [IsAuthenticated]
     def post(self, request, pk, format=None):
        print(pk)
        if( pk is not None):
            alumno = Alumno.objects.get(id = self.kwargs['pk'])
            cinturon = Alumno.objects.get(Nombre="B")
            if (alumno.kyu=="B" or alumno.kyu=="BA"): 
                kyu=1
            elif (alumno.kyu=="A" or alumno.kyu=="AN"): 
                kyu=2
            elif (alumno.kyu=="N" or alumno.kyu=="NV"): 
                kyu=3
            elif (alumno.kyu=="V" or alumno.kyu=="VAZ"): 
                kyu=4
            elif (alumno.kyu=="AZ" or alumno.kyu=="AM"): 
                kyu=5
            # partes = ParteExamen.objects.filter(Alum=cinturon)
            for i in range(kyu):
                print(i)
                if (i == 0 ): 
                    cinturon = Alumno.objects.get(Nombre="B")
                elif (i == 1): 
                    cinturon = Alumno.objects.get(Nombre="A")
                elif (i == 2): 
                    cinturon = Alumno.objects.get(Nombre="N")
                elif (i == 3): 
                    cinturon = Alumno.objects.get(Nombre="V")
                elif (i == 4): 
                    cinturon = Alumno.objects.get(Nombre="AZ")
                partes = ParteExamen.objects.filter(Alum=cinturon)
                for x in partes:
                    x.Alum=alumno
                    x.pk=None
                    x.save()
            alumno.FechaInicioExamen= datetime.now()
            alumno.examenActivo=True
            alumno.save()
        return Response(pk)

class FinalizacionExamen_API(RetrieveAPIView):
     permission_classes = [IsAuthenticated]
     def post(self, request, pk, format=None):
        print(pk)
        kyus =['B','BA','A','AN','N','NV','V','VAZ','AZ','AZM','M']
        if( pk is not None):
            alumno = Alumno.objects.get(id = self.kwargs['pk'])
            cinturon = alumno.kyu
            print(cinturon)
            for i in range(len(kyus)):
                if ( kyus[i] == cinturon):
                    alumno.kyu =kyus [i+1]
                    print(alumno.kyu)
                    alumno.FechaUltimoExamen= datetime.now()
            alumno.examenActivo=False
            alumno.FechaInicioExamen=None
            alumno.save()
            partes = ParteExamen.objects.filter(Alum=alumno)
            for x in partes:
                x.delete()
            historial = HistorialExamenes(Alumno=alumno,Fecha=datetime.now(),Kyu=cinturon)
            historial.save()
        return Response(pk)

class Alumnos_API(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None, *args, **kwargs):
        alumnos = Alumno.objects.filter(Activado=True)
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlumnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BSD_REQUEST)

class Tutores_API(APIView):
    
    def get(self, request, format=None, *args, **kwargs):
        tutores = Tutor.objects.all()
        serializer = TutorModelSerializar(tutores, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TutorModelSerializar(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BSD_REQUEST)

class PartesExamen_API(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None, *args, **kwargs):
        parteExamen = ParteExamen.objects.all()
        serializer = ParteExamenSerializer(parteExamen, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        parte=ParteExamen.objects.get(id=pk) # Le pasamos el que estamos usando para realizar update
        serializer = ParteExamenSerializer(parte, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Partes_API(APIView):
    def get(self, request, format=None, *args, **kwargs):
        parte = Parte.objects.all()
        serializer = ParteSerializer(parte, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ParteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BSD_REQUEST)

class Hisotial_API(APIView):
    def get(self, request, format=None, *args, **kwargs):
        historial = HistorialExamenes.objects.all()
        serializer = HistorialSerializer(historial, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HistorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BSD_REQUEST)



class Videos_API(APIView):
    
    def get(self, request, format=None, *args, **kwargs):
        videos = OnlineParts.objects.all()
        serializer = VideosSerialzier(videos, many=True)
        return Response(serializer.data)

    def post(self, request,  format=None):
        serializer = VideosSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Alumnos_API_DETAIL(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Alumno.objects.get(id=pk)
        except Alumno.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        alumno = Alumno.objects.get(id=pk)
        serializer = AlumnoSerializer(alumno)
        return Response(serializer.data)
    
    def post(self, request, pk, format=None):
        al = self.get_object(pk)
        serializer = AlumnoSerializer(al, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        al= self.get_object(pk)
        al.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Login_API(ObtainAuthToken):


    def post(self,request,*args,**kwargs):
        print(request.data)
        login_serializer = self.serializer_class(data = request.data, context= {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            print('paso verificacion---------------')
            token = Token.objects.get_or_create(user=user)
            tutor = Tutor.objects.get(user=user)
            serializer = TutorModelSerializar(tutor)
            print(tutor.id)
            return Response({'token': token[0].key,'Tutor':serializer.data})
        return Response({'mensaje':'Response'},status=status.HTTP_401_UNAUTHORIZED)

class RegisterApi(APIView):
    def get(self, request, format=None):
        return Response({'detail':"GET Response"})
    
    def post(self, request, format=None):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.update()
            serializer.save()
            return Response(serializer.data)
        return Response('No se realizo')