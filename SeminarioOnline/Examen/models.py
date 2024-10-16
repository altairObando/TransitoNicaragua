from django.db import models


# Create your models here.
class Categoria(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)

    def __str__(self) -> str:
        return '{0} {1}'.format(self.codigo, self.nombre)

    def total_preguntas(self) -> int:
        return Pregunta.objects.filter(categoria__id=self.id).count()


class Pregunta(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=500)
    image_url = models.ImageField(upload_to='uploads/', null=True)

    def __str__(self) -> str:
        return self.pregunta

    def total_respuestas(self) -> int:
        return Respuesta.objects.filter(pregunta__id=self.id).count()

    class Meta:
        verbose_name = 'Pregunta'


class Respuesta(models.Model):
    texto = models.CharField(max_length=250)
    esCorrecta = models.BooleanField(default=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='uploads/', null=True)

    def __str__(self) -> str:
        return self.texto
