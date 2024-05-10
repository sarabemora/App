from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from .logic import consultas_logic as cl
import json
from .forms import ConsultasForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from app.auth0backend import getRole

@login_required
@csrf_exempt
def consultas_view(request):
    role = getRole(request)
    if role == "Admin":
        if request.method == 'GET':
            form = ConsultasForm()
            return render(request, 'Consulta/consultas.html', {'form': form})
    
        if request.method == 'POST':
            cedula = request.POST.get('id')
            consulta = cl.get_consulta_by_cedula(cedula)
            return render(request, 'Consulta/consultas.html', {'consulta': consulta})
    else:
        return HttpResponse("No tienes permisos para ver esta página")

