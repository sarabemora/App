from ..models import Inicio

def get_login(cedula, password):
    inicio = Inicio.objects.get(cedula=cedula, password=password)
    return inicio