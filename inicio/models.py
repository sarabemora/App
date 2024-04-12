from django.db import models

class Inicio(models.Model):
    cedula = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.cedula