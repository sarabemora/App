from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.login_view, name='login_view'),
    #path('', views.login_view, name='login_view'),
]