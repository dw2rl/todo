# Imports
from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todos, name='todos'),
    path('todos/<int:pk>/', views.todo, name='todo'),
    path('todos/add-todo/', views.add_todo, name='add-todo'),
    path('todos/update-todo/<int:pk>/', views.update_todo, name='update-todo'),
    path('todos/delete-todo/<int:pk>/', views.delete_todo, name='delete-todo')
]
