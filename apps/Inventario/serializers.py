from rest_framework import serializers

from .models import Marca, Categoria, Referencia, Elemento


class MarcaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Marca
		fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = '__all__'


class ReferenciaSerializer(serializers.ModelSerializer):
	marca = serializers.SerializerMethodField('get_marcas')

	class Meta:
		model = Referencia
		fields = '__all__'

	def get_marcas(self, obj):
		return obj.marca.name


class ReferenciaStoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Referencia
		fields = '__all__'


class ElementoSerializerPreview(serializers.ModelSerializer):
	referencia = serializers.SerializerMethodField('get_referencia')

	class Meta:
		model = Elemento
		fields = ('placa', 'referencia', 'modelo', 'estado')

	def get_referencia(self, obj):
		return f'{obj.referencia.categoria.name} - {obj.referencia.marca.name}'


class ElementoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Elemento
		fields = '__all__'


class ElementoViewSerializer(serializers.ModelSerializer):
	referencia = serializers.SerializerMethodField('get_referencia')
	proveedor = serializers.SerializerMethodField('get_proveedor')

	class Meta:
		model = Elemento
		fields = '__all__'

	def get_referencia(self, obj):
		return f'{obj.referencia.categoria.name} - {obj.referencia.marca.name}'

	def get_proveedor(self, obj):
		return f'{obj.proveedor.NIT} - {obj.proveedor.razonSocial}'
