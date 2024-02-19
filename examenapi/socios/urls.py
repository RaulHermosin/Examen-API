from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('añadirusuario/', views.añadirusuario),
    path('actualizarcontra/', views.actualizar),
    path('usuarios/', views.verusuario),
]