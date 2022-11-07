# Imports
from django.shortcuts import render
# from django.http import HttpResponse

from .models import ToDo


def index(request):
    todos = ToDo.objects.all()

    return render(request, 'base/home.html', {'todos': list(todos)})


def todo(request, pk):
    todo = ToDo.objects.get(id=pk)
    return render(request, 'base/todo.html', {'todo': todo})
