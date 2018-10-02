from django.urls import include, path, re_path
from django.contrib import admin
from homepage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('sawtooth/', views.sawtooth, name='sawtooth'),
    path('mentors/', views.mentors, name='mentors'),
    path('oilbarn/', views.oilbarn, name='oilbarn'),
    path('pixingo/', views.pixingo, name='pixingo'),
    path('boda/', views.boda, name='boda'),
    path('xlr8/', views.xlr8, name='xlr8'),
    path('parentiq/', views.parentiq, name='parentiq'),
]
