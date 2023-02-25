from django.shortcuts import render, redirect
from .models import *
from .forms import * 
from django.http import HttpResponse
from tkinter import *
from tkinter import messagebox as MessageBox


# vista para el logo
def layout(request):
    context={}
    return render(request,'layout.html',context)

#Vista inicial, muestra los cursos
def home(request):
    Curso=gestionCursos.objects.all()
    context={'Curso':Curso}
    return render(request,'home.html',context)

#Vista para agregar un curso
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

#Vista para editar un curso
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

#Vista para eliminar un curso
def eliminar(request,curso_id):
    Curso=gestionCursos.objects.get(id=curso_id)
    Curso.delete()
    return redirect('home')

#vista para listar los departamentos
def homedpto(request):
    Dptos=Dpto.objects.all()
    context={'Dptos':Dptos}
    return render(request,'Deptor.html',context)

#Vista para eliminar un departamento
def eliminarDpto(request,dpto_id):
    Depto=Dpto.objects.get(id=dpto_id)
    consulta=gestionCursos.objects.filter(nombreDpto=dpto_id)
    if consulta:
        MessageBox.showerror("Error", 
    "El departamento tiene cursos asignados.")
        return redirect('homedpto')
    else:
        resultado = MessageBox.askquestion("Eliminar", 
    "¿Está seguro que desea Eliminar este departamento?")

        if resultado == "yes":
            Depto.delete()
            MessageBox.showerror("OK", 
            "El departamento ha sido eliminado.")
    return redirect('homedpto')

#vista para agregar un departamento
def agregarDptos(request):
    if request.method=="POST":
        formDpto= agregarDpto(request.POST)
        if formDpto.is_valid():
            formDpto.save()
            return redirect('homedpto')
    else:
        formDpto=agregarDpto()
    context={'formDpto':formDpto}
    return render(request,'agregarDpto.html',context)

def editarDpto(request,dpto_id):
    Depto=Dpto.objects.get(id=dpto_id)
    if request.method=="POST":
        dpto=agregarDpto(request.POST, instance=Depto)
        if dpto.is_valid():
            dpto.save()
        return redirect("homedpto")
    else:
        dpto=agregarDpto(instance=Depto)
    context={"dpto":dpto}
    return render(request,"editarDpto.html",context)