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

def update_consulta(id, new_id):
    consulta = get_consulta(id)
    consulta.cedula = new_id['cedula']
    consulta.save()
    return consulta

def get_consulta_by_cedula(cedula):
    consulta = Consulta.objects.get(cedula=cedula)
    return consulta
