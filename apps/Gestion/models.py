from django.db import models

from ..Inventario.models import Elemento
from ..Personas.models import Funcionario


class Asignacion(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    timestamps = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Asignacion"
        verbose_name_plural = "Asignaciones"

    def __str__(self):
        return f'{self.funcionario} {self.user}'


class DetallesAsignacion(models.Model):
    asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE)
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)
    timestamps = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "DetallesAsignacion"
        verbose_name_plural = "DetallesAsignaciones"

    def __str__(self):
        return f'{self.asignacion} {self.elemento}'


class Mantenimiento(models.Model):
    PID = models.AutoField(primary_key=True)
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    fechaFin = models.DateTimeField(null=True, blank=True)
    descripcion = models.CharField(max_length=50000)
    observaciones = models.CharField(max_length=50000)
    timestamps = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=100, default="En Progreso")

    def __str__(self):
        return f'{self.PID} {self.elemento}'


class Baja(models.Model):
    PID = models.AutoField(primary_key=True)
    user = models.CharField(max_length=10)
    timestamps = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.PID}'


class DetalleBaja(models.Model):
    baja = models.ForeignKey(Baja, on_delete=models.CASCADE)
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)
    autorizado = models.BooleanField(default=True)
    timestamps = models.DateTimeField(auto_now=True)
    fechaBorrado = models.DateField()

    def __str__(self):
        return f'{self.baja} {self.elemento}'
