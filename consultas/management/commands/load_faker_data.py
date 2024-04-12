from consultas.models import Consulta
from faker import Faker
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(200000):   
            Consulta.objects.create(
                nombre=fake.name(),
                tipo_doc=fake.random_element(elements=('CC', 'TI', 'Pasaporte')),
                cedula=fake.random_number(digits=8),
                telefono=fake.phone_number(),
                correo=fake.email(),
                pais=fake.country(),
                ciudad=fake.city()
            )