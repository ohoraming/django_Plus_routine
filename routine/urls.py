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
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('routine_form/', views.renderRoutineForm, name='renderRoutineForm'),
    path('readAll/<int:user_id>', views.readAll, name='readAll'),
    path('readOne/<int:routine_id>', views.readOne, name='readOne'),
    path('loadResult/<int:routine_day_id>', views.loadResult, name='loadResult'),
    path('delete/<int:routine_id>/<int:routine_day_id>', views.deleteRoutine, name='deleteRoutine'),
    path('update/<int:routine_id>', views.updateRoutine, name='updateRoutine'),
]
