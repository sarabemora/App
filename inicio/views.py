from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .logic import inicio_logic as il
from app.auth0backend import getRole
from django.contrib.auth.decorators import login_required

@login_required
def login_view(request):
    role = getRole(request)
    if role == 'Admin':
        if request.method == 'POST':
            id = request.POST.get('id')
            passwords = request.POST.get('password')
            inicio = il.get_login(id, passwords)
            return render(request, 'Inicio/inicios.html', {'inicio': inicio})

        if request.method == 'GET':
            form = LoginForm()
            return render(request, 'Inicio/inicios.html', {'form': form})
        else:
            form = LoginForm()
        return render(request, 'Inicio/inicios.html', {'form': form})
    else:
        return HttpResponse("No tienes permisos para ver esta página")