from django import forms
from .models import *


class agregarCurso(forms.ModelForm):
    class Meta:
        model= gestionCursos
        fields=('nomCurso','descripcion','duracion','estado','nombreDpto')

