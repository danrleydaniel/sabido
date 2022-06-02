from django.shortcuts import render, redirect
from .forms import CursoForm
from .models import Curso

# Create your views here.

def curso_list(request):
    context = {'curso_list':Curso.objects.all()}
    return render(request, "curso/curso_list.html", context)

def curso_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = CursoForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados do Tarefa correspondentes à chave primária referente ao id
            curso = Curso.objects.get(pk = id)
            form = CursoForm(instance = curso)
        return render(request, "curso/curso_form.html", {'form': form})
    else:
        if id == 0: # Operação de inserir uma nova Tarefa
            form = CursoForm(request.POST)
        else: # Operação de atualizar uma Tarefa já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            curso = Curso.objects.get(pk = id)
            form = CursoForm(request.POST, instance = curso)
        if form.is_valid(): 
            form.save()
        return redirect('/curso/list')            

def curso_delete(request, id):
    curso = Curso.objects.get(pk = id)
    curso.delete()
    return redirect('/curso/list')

