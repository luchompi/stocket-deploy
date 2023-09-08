from apps.Personas.models import Proveedores
from django.db import models


class Marca(models.Model):
	name = models.CharField(max_length=50, verbose_name="Nombre", unique=True,
	                        error_messages={'unique': "Ya existe una marca con este nombre"})
	description = models.TextField(verbose_name="Descripción", null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

	class Meta:
		verbose_name = "Marca"
		verbose_name_plural = "Marcas"

	def __str__(self) -> str:
		return f'{self.name}'


class Categoria(models.Model):
	name = models.CharField(max_length=50, verbose_name="Nombre", unique=True,
	                        error_messages={'unique': "Ya existe una categoria con este nombre"})
	description = models.TextField(verbose_name="Descripción", null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Categoria"
		verbose_name_plural = "Categorias"

	def __str__(self) -> str:
		return f'{self.name}'


class Referencia(models.Model):
	marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca")
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
	timestamps = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Referencia"
		verbose_name_plural = "Referencias"

	def __str__(self) -> str:
		return f'{self.marca} - {self.categoria}'


class Elemento(models.Model):
	placa = models.BigAutoField(primary_key=True, verbose_name="Placa")
	referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE, verbose_name="Referencia")
	modelo = models.CharField(max_length=50, verbose_name="Tipo", null=True, blank=True)
	serial = models.CharField(max_length=50, verbose_name="Serial", unique=True,
	                          error_messages={'unique': "Ya existe un elemento con este serial"})
	estado = models.CharField(verbose_name="Estado", default='Por asignar', max_length=50)
	IP = models.GenericIPAddressField(verbose_name="IP", null=True, blank=True, unique=True,
	                                  error_messages={'unique': "La IP está en uso"})
	MAC = models.CharField(max_length=50, verbose_name="MAC", unique=True, null=True, blank=True,
	                       error_messages={'unique': 'Ya existe un elemento con esta MAC'})
	proveedor = models.ForeignKey(Proveedores, on_delete=models.SET_NULL, null=True, blank=True,
	                              verbose_name="Proveedor")
	created_at = models.DateTimeField(auto_now_add=True)
	delete_on = models.DateTimeField(null=True, blank=True)
	created_by = models.CharField(max_length=50, verbose_name="Creado por", default='admin')

	class Meta:
		verbose_name = "Elemento"
		verbose_name_plural = "Elementos"

	def __str__(self) -> str:
		return f'{self.placa} - {self.referencia} - {self.estado}'
