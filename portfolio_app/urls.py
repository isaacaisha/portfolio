# /home/siisi/portfolio/app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/add/', views.project_create, name='project_create'),
    path('notifications/',   views.notifications,  name='notifications'),
]
