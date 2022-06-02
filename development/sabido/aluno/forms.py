from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = {'nome', 'dataNasc', 'email'}
        labels = {
            'nome':'Nome do aluno',
            'dataNasc':'Data de Nascimento',
            'email':'Email'
        }
