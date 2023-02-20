from django import forms
from .models import *


class agregarCurso(forms.ModelForm):
    class Meta:
        model= gestionCursos
        fields=['nomCurso']
        fields=['descripcion']
        fields=['duracion']
        Fields=['estado']
        fields=['nombreDpto']