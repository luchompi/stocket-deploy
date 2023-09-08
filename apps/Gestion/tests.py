from django.test import TestCase
from .models import Funcionario, Asignacion, DetallesAsignacion,Mantenimiento,Baja,DetalleBaja
from apps.Inventario.models import Elemento, Referencia, Marca, Categoria

class ModelTestCase(TestCase):
    def setUp(self):
        # Crear objetos relacionados
        self.marca = Marca.objects.create(name='Marca1')
        self.categoria = Categoria.objects.create(name='Categoria1')
        self.referencia = Referencia.objects.create(marca=self.marca, categoria=self.categoria)
        
        self.funcionario = Funcionario.objects.create(
            iden='12345',
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            phone='1234567890',
            address='123 Main St',
            job='Developer'
        )
        
        self.elemento = Elemento.objects.create(
            placa=1,
            referencia=self.referencia,
            serial='Serial123',
            estado='Por asignar',
            created_by='admin'
        )
        
        self.asignacion = Asignacion.objects.create(
            funcionario=self.funcionario,
            user='test_user'
        )
        
        self.detalle_asignacion = DetallesAsignacion.objects.create(
            asignacion=self.asignacion,
            elemento=self.elemento
        )

        self.mantenimiento = Mantenimiento.objects.create(
            elemento=self.elemento,
            user='test_user',
            descripcion='Descripción del mantenimiento',
            observaciones='Observaciones del mantenimiento'
        )
        
        self.baja = Baja.objects.create(
            user='test_user'
        )
        
        self.detalle_baja = DetalleBaja.objects.create(
            baja=self.baja,
            elemento=self.elemento,
            fechaBorrado='2023-08-10'
        )
        
    def test_funcionario_creation(self):
        funcionario = Funcionario.objects.get(iden='12345')
        self.assertEqual(funcionario.first_name, 'John')
        
    def test_elemento_creation(self):
        elemento = Elemento.objects.get(serial='Serial123')
        self.assertEqual(elemento.referencia.marca.name, 'Marca1')
        
    def test_asignacion_relation(self):
        asignacion = self.funcionario.asignacion_set.first()
        self.assertEqual(asignacion.user, 'test_user')
        
    def test_detalle_asignacion_relation(self):
        detalle_asignacion = self.asignacion.detallesasignacion_set.first()
        self.assertEqual(detalle_asignacion.elemento.serial, 'Serial123')

    def test_elemento_estado(self):
        elemento = Elemento.objects.get(serial='Serial123')
        self.assertEqual(elemento.estado, 'Por asignar')

    def test_referencia_str(self):
        referencia = Referencia.objects.get(pk=self.referencia.pk)
        expected_str = f'{referencia.marca} - {referencia.categoria}'
        self.assertEqual(str(referencia), expected_str)
    
    
    def test_mantenimiento_creation(self):
        mantenimiento = Mantenimiento.objects.get(user='test_user')
        self.assertEqual(mantenimiento.descripcion, 'Descripción del mantenimiento')

    def test_baja_creation(self):
        baja = Baja.objects.get(user='test_user')
        self.assertIsNotNone(baja)

    def test_detalle_baja_relation(self):
        detalle_baja = DetalleBaja.objects.get(baja=self.baja)
        self.assertEqual(detalle_baja.elemento.serial, 'Serial123')