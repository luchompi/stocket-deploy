from rest_framework import serializers

from .models import Asignacion, DetallesAsignacion, Mantenimiento, Baja, DetalleBaja


class AsignacionSerializer(serializers.ModelSerializer):
    funcionario = serializers.SerializerMethodField('get_funcionario')

    class Meta:
        model = Asignacion
        fields = '__all__'

    def get_funcionario(self, obj):
        return [{'iden': obj.funcionario.iden, 'first_name': obj.funcionario.first_name,
                 'last_name': obj.funcionario.last_name}]


class DetallesAsignacionSerializer(serializers.ModelSerializer):
    elementos = serializers.SerializerMethodField('get_element')

    class Meta:
        model = DetallesAsignacion
        fields = '__all__'

    def get_element(self, obj):
        return [
            {
                'placa': obj.elemento.placa,
                'referencia': f'{obj.elemento.referencia.categoria.name} - {obj.elemento.referencia.marca.name}',
                'modelo': obj.elemento.modelo,
                'estado': obj.elemento.estado,
            }
        ]


class MantenimientoSerializer(serializers.ModelSerializer):
    elemento = serializers.SerializerMethodField('get_element')

    class Meta:
        model = Mantenimiento
        fields = '__all__'

    def get_element(self, obj):
        return [
            {
                'placa': obj.elemento.placa,
                'referencia': f'{obj.elemento.referencia.categoria.name} - {obj.elemento.referencia.marca.name}',
                'modelo': obj.elemento.modelo,
            }
        ] if obj.elemento else None


class BajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baja
        fields = '__all__'


class DetalleBajaSerializer(serializers.ModelSerializer):
    elemento = serializers.SerializerMethodField('get_element')

    class Meta:
        model = DetalleBaja
        fields = '__all__'

    def get_element(self, obj):
        return [
            {
                'placa': obj.elemento.placa,
                'referencia': f'{obj.elemento.referencia.categoria.name} - {obj.elemento.referencia.marca.name}',
                'modelo': obj.elemento.modelo,
            }
        ] if obj.elemento else None
