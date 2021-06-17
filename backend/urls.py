"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from nucleo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createExamen/', VistaCrearExamen.as_view(), name="crear_examen"),
    path('asignarExamen/', VistaAsignarExamen.as_view(), name="asignar_examen"),
    path('asignacion/<int:pk>',AsignacionExamen.as_view(),name="asignacion"),
    path('verExamen/<int:pk>',VerExamen.as_view(),name="verEx"),
    #API
    path('api/alumnos/',Alumnos_API.as_view(),name="alumnos_api"),
    path('api/alumnos/<int:pk>',Alumnos_API_DETAIL.as_view(),name="alumnos_api_detail"),
    path('api/asignacion/<int:pk>',AsginacionExamen_API.as_view(),name="alumnos_asignacion"),
    path('api/finalizacion/<int:pk>',FinalizacionExamen_API.as_view(),name="alumnos_finalizacion"),
    path('api/tutores/',Tutores_API.as_view(),name="tutores_api"),
   # path('api/tutores/<int:pk>',Tutores_API.as_view(),name="alumnos_api_detail"),
    path('api/videos/',Videos_API.as_view(),name="videos_api"),
    path('api/historial/',Hisotial_API.as_view(),name="historial_api"),
    path('api/partesExamen/',PartesExamen_API.as_view(),name="partesExamen_api"),
    path('api/partes/',Partes_API.as_view(),name="partes_api"),
    path('api/partes/<int:pk>',PartesExamen_API.as_view(),name="partes_asignacion"),
    path('api/token/',Login_API.as_view(),name="test_api"),
    path('api/register/',RegisterApi.as_view(),name="register_api"),

]
