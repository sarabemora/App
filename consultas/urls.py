from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('consultas/', views.consultas_view, name='consultas_view'),
    path('', views.consultas_view, name='consultas_view'),
]