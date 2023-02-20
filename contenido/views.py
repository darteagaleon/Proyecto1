from django.shortcuts import render, redirect
from .models import *
from .forms import agregarCurso
# Create your views here.
def home(request):
    Curso=gestionCursos.objects.all()
    context={'Curso':Curso}
    return render(request,'home.html',context)

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