from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('utils', views.utils, name='utils'),
    path('projects', views.projects, name='projects'),
    path('other', views.other, name='other'),
]