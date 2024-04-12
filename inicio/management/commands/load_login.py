from inicio.models import Inicio
from faker import Faker
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(200):   
            Inicio.objects.create(
            cedula=str(fake.unique.random_number(digits=10)),  
            password=fake.password(length=10)
        )