# urls.py
from django.urls import path
from .views import cargar_preguntas_view

urlpatterns = [
    path('cargar_preguntas/', cargar_preguntas_view, name='cargar_preguntas'),
]
