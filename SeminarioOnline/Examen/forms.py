# forms.py
from django import forms


class CargarPreguntasForm(forms.Form):
    archivo = forms.FileField()
