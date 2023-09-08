from rest_framework import serializers

from .models import Funcionario, Proveedores


class FuncionarioPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('iden', 'first_name', 'last_name', 'status')


class FuncionarioSerializer(serializers.ModelSerializer):
    sede = serializers.SerializerMethodField('get_sede_name')

    class Meta:
        model = Funcionario
        fields = '__all__'

    def get_sede_name(self, obj):
        return obj.sede.name if obj.sede else None


class FuncionarioStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'
