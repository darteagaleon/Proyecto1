from django.db import models

# Create your models here.
#Se crea el modelo de la tabla de las areas de la empresa
class Dpto(models.Model):
    nombreDpto=models.CharField(max_length=100)
    def __str__(self):
        return self.nombreDpto

#Se crea el modelo de la tabla gestion de cursos donde se encontrara 
#la informacion basica de los cursos registrados
class gestionCursos(models.Model):
    nomCurso=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=1000)
    duracion=models.CharField(max_length=3)
    estado=models.BooleanField(default=False)
    #Se crea la relacion
    nombreDpto=models.ForeignKey(Dpto, on_delete=models.CASCADE, null=False)
    #Este metodo sirve para mostrar el nombre que nosotros le hemos puesto
    #y no el valor en memoria
    def __str__(self):
        return self.nomCurso


