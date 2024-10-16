from django.contrib import admin

from .models import Categoria, Pregunta, Respuesta


# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo', 'nombre', 'observaciones', 'total_preguntas']
    ordering = ['id']


@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ['id', 'pregunta__categoria', 'texto', 'esCorrecta', ]
    ordering = ['id']


class RespuestaInline(admin.TabularInline):
    model = Respuesta
    fields = ['texto', 'esCorrecta']


class PreguntaAdmin(admin.ModelAdmin):
    inlines = [
        RespuestaInline
    ]
    list_display = ['id', 'categoria', 'pregunta', 'total_respuestas']
    ordering = ['id', 'categoria']
    search_fields = ['pregunta']


admin.site.register(Pregunta, PreguntaAdmin)
