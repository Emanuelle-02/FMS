from django.forms import ModelForm
from .models import Categoria
from django import forms

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome"]