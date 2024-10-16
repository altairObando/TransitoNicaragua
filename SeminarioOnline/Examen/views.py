# views.py
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pregunta, Respuesta, Categoria
from .forms import CargarPreguntasForm

def cargar_preguntas_view(request):
    if request.method == 'POST':
        form = CargarPreguntasForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            data = json.load(archivo)

            categorias_dict = {categoria.id: categoria for categoria in Categoria.objects.all()}

            preguntas = []
            respuestas = []

            # Primero, creamos las preguntas
            for item in data:
                categoria_id = int(item['categoria'])
                pregunta_texto = item['pregunta']
                if categoria_id in categorias_dict:
                    pregunta = Pregunta(categoria=categorias_dict[categoria_id], pregunta=pregunta_texto)
                    preguntas.append(pregunta)

            # Guardamos las preguntas en bulk
            Pregunta.objects.bulk_create(preguntas)

            # Ahora asociamos las respuestas a sus respectivas preguntas
            for i, item in enumerate(data):
                pregunta = preguntas[i]  # Obtenemos la pregunta recién creada
                for respuesta in item['respuestas']:
                    # Creamos la respuesta y la asociamos a la pregunta
                    respuestas.append(Respuesta(texto=respuesta['texto'], esCorrecta=respuesta['correcto'], pregunta=pregunta))

            # Guardamos las respuestas en bulk
            Respuesta.objects.bulk_create(respuestas)

            return HttpResponse('Preguntas y respuestas cargadas exitosamente')
    else:
        form = CargarPreguntasForm()

    return render(request, 'cargar_preguntas.html', {'form': form})
