from django.urls import URLPattern, path, include
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.formulario, name='formulario'),
    path('valido/', views.valido, name='valido'),
    path('registro/',views.registro, name='registro'),
    path('comentario/', views.comentario, name='comentario'),
]
