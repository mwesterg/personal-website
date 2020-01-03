from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('utils', views.utils, name='utils'),
    path('projects', views.projects, name='projects'),
    path('other', views.other, name='other'),
    path('about',views.about, name='about'),
    path('contact',views.about, name='contact'),
]