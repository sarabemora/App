from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from .logic import consultas_logic as cl
import json
from .forms import ConsultasForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def consultas_view(request):
    if request.method == 'GET':
        form = ConsultasForm()
        return render(request, 'Consulta/consultas.html', {'form': form})
    
    if request.method == 'POST':
        cedula = request.POST.get('id')
        consulta = cl.get_consulta_by_cedula(cedula)
        return render(request, 'Consulta/consultas.html', {'consulta': consulta})
 