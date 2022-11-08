# Imports
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from .models import ToDo
from .forms import ToDoForm


def todos(request):
    todos = ToDo.objects.all()

    return render(request, 'base/home.html', {'todos': list(todos)})


def todo(request, pk):
    todo = ToDo.objects.get(id=pk)
    return render(request, 'base/todo.html', {'todo': todo})


def add_todo(request):
    form = ToDoForm()
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
    else:
        form = ToDoForm()
    context = {'form': form}
    return render(request, 'base/add_update_todos.html', context)


def update_todo(request, pk):
    todo = ToDo.objects.get(id=pk)
    form = ToDoForm(instance=todo)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos')
    context = {'todo': todo, 'form': form}
    return render(request, 'base/add_update_todos.html', context)


def delete_todo(request, pk):
    todo = ToDo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos')
    return render(request, 'base/delete_todo.html', {'todo': todo})
