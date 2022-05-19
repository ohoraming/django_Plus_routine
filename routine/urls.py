"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from routine import views

app_name = 'routine'

urlpatterns = [
    # Create
    path('create/', views.create, name='create'),
    
    # Read
    path('', views.index, name='index'),
    path('routine_form/', views.renderRoutineForm, name='renderRoutineForm'),
    path('readAll/', views.readAll, name='readAll'),
    path('readOne/<int:routine_id>/', views.readOne, name='readOne'),
    path('Result/<int:routine_id>/', views.updateResult, name='updateResult'),
    
    # Update
    path('update/<int:routine_id>/', views.updateRoutine, name='updateRoutine'),
    path('updateResult/<int:routine_id>/', views.updateResult, name='updateResult'),
    
    # Delete
    path('delete/<int:user_id>/<int:routine_id>/', views.deleteRoutine, name='deleteRoutine'),
    path('deleteDay/<int:routine_id>/<int:routine_day_id>', views.deleteDay, name='deleteDay'),
]
