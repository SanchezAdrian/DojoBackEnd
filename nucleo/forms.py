from nucleo.models import *
from django import forms

class CreacionExamenForm(forms.ModelForm):
    class Meta:
        model = ParteExamen
        
        fields=('Part','Realizadas','Nota','Finalizada','Alum','Info')
