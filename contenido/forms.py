from django import forms
from .models import *


class agregarCurso(forms.ModelForm):
    class Meta:
        model= gestionCursos
        fields=('nomCurso','descripcion','duracion','estado','nombreDpto')

class agregarDpto(forms.ModelForm):
    class Meta:
        model= Dpto
        fields=('nombreDpto',)