from django.contrib import admin
from .models import *

#Se registran los modelos para poder visializarlos en el admin de django
#Se crea una clase donde se muestran los elementos a listar
#en la linea 9 se coloca el nombre del modelo y el nombre de la clase
class Area(admin.ModelAdmin):
    list_display=['id','nombreDpto']
admin.site.register(Dpto,Area)

class regCursos(admin.ModelAdmin):
    list_display=['id','nomCurso','descripcion','nombreDpto']
admin.site.register(gestionCursos, regCursos)

