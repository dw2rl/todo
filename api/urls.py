from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('todos/', views.getData, name='todos'),
    path('todos/add/', views.addData, name='add'),
    path('todos/<int:pk>/', views.todoView, name='detail'),
    path('todos/update/<int:pk>/', views.updateData, name='update'),
    path('todos/delete/<int:pk>/', views.deleteData, name='delete')
]
