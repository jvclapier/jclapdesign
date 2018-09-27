from django.urls import include, path, re_path
from django.contrib import admin
from homepage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
]
