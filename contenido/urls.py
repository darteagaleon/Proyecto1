from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('agregar/', views.agregar,name="agregar"),
    path('layout/', views.layout,name="layout"),
    

    
    path('eliminar/<int:curso_id>/', views.eliminar,name="eliminar"),
    path('editar/<int:curso_id>/', views.editar,name="editar"),
    #URL Departamentos
    path('homedpto/', views.homedpto,name="homedpto"),
    path('eliminarDpto/<int:dpto_id>/', views.eliminarDpto,name="eliminarDpto"),
    path('editarDpto/<int:dpto_id>/', views.editarDpto,name="editarDpto",),
    path('agregarDpto/', views.agregarDptos,name="agregarDpto"),
    # path('editarDpto/', views.editarDpto, name="editarDpto"),

    


]
