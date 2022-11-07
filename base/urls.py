# Imports
from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.index, name='index'),
    path('todos/<int:pk>/', views.todo, name='todo')
]
