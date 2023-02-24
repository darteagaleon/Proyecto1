from django.shortcuts import render, redirect
from .models import *
from .forms import agregarCurso
from django.http import HttpResponse
from tkinter import *
from tkinter import messagebox as MessageBox


# Create your views here.
def layout(request):
    context={}
    return render(request,'layout.html',context)

def home(request):
    Curso=gestionCursos.objects.all()
    context={'Curso':Curso}
    return render(request,'home.html',context)

#Vista Principal de Dpto
def Departa(request):
    Depa=Dpto.objects.all()
    context={'Depa':Depa}
    return render(request,'Deptor.html',context)


def agregar(request):
    if request.method=="POST":
        form= agregarCurso(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form= agregarCurso()
    context={'form':form}
    return render(request,'agregar.html',context)

#VISTAS DE CURSO
def editar(request,curso_id):
    Curso=gestionCursos.objects.get(id=curso_id)
    if request.method=="POST":
        form=agregarCurso(request.POST, instance=Curso)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form=agregarCurso(instance=Curso)
    context={"form":form}
    return render(request,"editar.html",context)

def eliminar(request,curso_id):
    Curso=gestionCursos.objects.get(id=curso_id)
    Curso.delete()
    return redirect('home')
#VISTAS DE DEPARTAMENTO
def eliminarDpto(request,dpto_id):
    Depto=Dpto.objects.get(id=dpto_id)
    print(Depto)

    Curso=gestionCursos.objects.get(nombreDpto_id=dpto_id)
    print(Curso)

    if Curso:
        MessageBox.showerror("Error", 
    "Este departamento no se puede eliminar porque tiene cursos asociados")
        # return redirect('Deptor')
    else:
     Depto.delete()
     return redirect('Deptor')
# def editarDpto(request,curso_id):
#     Curso=gestionCursos.objects.get(id=curso_id)
#     if request.method=="POST":
#         form=agregarCurso(request.POST, instance=Curso)
#         if form.is_valid():
#             form.save()
#         return redirect("Dpto.html")
#     else:
#         form=agregarCurso(instance=Curso)
#     context={"form":form}
#     return render(request,"editar.html",context)

