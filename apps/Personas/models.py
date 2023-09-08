from django.db import models
from apps.Empresa.models import Sede

class Funcionario(models.Model):
    iden = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    status = models.CharField(max_length=50,default='Activo')
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.iden} {self.first_name} {self.last_name}'

class Proveedores(models.Model):
    NIT = models.CharField(max_length=50, primary_key=True)
    razonSocial = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.NIT} {self.razonSocial}'