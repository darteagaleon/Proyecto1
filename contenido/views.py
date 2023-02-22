from django.shortcuts import render, redirect
from .models import *
from .forms import agregarCurso


# Create your views here.
def home(request):
    Curso=gestionCursos.objects.all()
    context={'Curso':Curso}
    return render(request,'home.html',context)

#Vista Principal de Dpto


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
    Depto.delete()
    return redirect('home')
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

