from django.contrib import admin
from nucleo.models import *
# Register your models here.

class ParteAdmin(admin.ModelAdmin):
    list_display = ['id', 'Categoria', 'Orientacion', 'Nombre'] 
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['id', 'Nombre'] 

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Tutor)
admin.site.register(Parte, ParteAdmin)
admin.site.register(ParteExamen)
admin.site.register(OnlineParts)
admin.site.register(HistorialExamenes)