from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    Curso=gestionCursos.objects.all()
    context={'Curso':Curso}
    return render(request,'home.html',context)