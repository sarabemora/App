from ..models import Consulta

def get_consultas():
    consultas = Consulta.objects.all()
    return consultas

def get_consulta(id):
    consulta = Consulta.objects.get(id=id)
    return consulta

def create_consulta(con):
    consulta = Consulta(cedula=con['cedula'])
    consulta.save()
    return consulta

def update_consulta(id, new_telefono):
    consulta = get_consulta(id)
    consulta.telefono = new_telefono
    consulta.save()
    return consulta

def get_consulta_by_cedula(cedula):
    consulta = Consulta.objects.get(cedula=cedula)
    return consulta
