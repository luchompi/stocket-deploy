from rest_framework import serializers

from .models import Dependencia, Empresa, Sede, SedeDependencia


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'

class DependenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependencia
        fields = '__all__'

class SedeDependenciaSerializer(serializers.ModelSerializer):
    dependencias = serializers.SerializerMethodField('get_dependencias')
    class Meta:
        model = SedeDependencia
        fields = '__all__'

    def get_dependencias(self, obj):
        return [{"id": obj.dependencia.id, "nombre": obj.dependencia.name}]