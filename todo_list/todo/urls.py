from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='list'),
    path('add/', views.add_todo, name='add'),
    path('toggle/<int:pk>/', views.toggle_todo, name='toggle'),
    path('delete/<int:pk>/', views.delete_todo, name='delete'),
    path('edit/<int:pk>/', views.edit_todo, name='edit'),
]
