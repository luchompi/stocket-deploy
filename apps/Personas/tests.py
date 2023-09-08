from django.test import TestCase
from .models import Funcionario,Proveedores
class FuncionarioTestCase(TestCase):
        def setUp(self):
            self.funcionario = Funcionario(
                iden='123',
                first_name='John',
                last_name='Doe',
                email='john.doe@example.com',
                phone='1234567890',
                address='123 Main St',
                job='Engineer',
                status='Activo',
                sede=None
            )
        
        def test_str_representation(self):
            self.assertEqual(str(self.funcionario), '123 John Doe')
        
        def test_iden_max_length(self):
            self.assertLessEqual(len(self.funcionario.iden), 50)
        
        def test_email_validity(self):
            self.assertTrue('@' in self.funcionario.email)
        
        def test_phone_max_length(self):
            self.assertEqual(len(self.funcionario.phone), 10)
        
        def test_job_max_length(self):
            self.assertLessEqual(len(self.funcionario.job), 50)
        
        def test_sede_nullability(self):
            self.assertIsNone(self.funcionario.sede)

        def test_status_max_length(self):
            self.assertLessEqual(len(self.funcionario.status), 50)

class ProveedoresTestCase(TestCase):
    def setUp(self):
        self.proveedores = Proveedores(
            NIT='123',
            razonSocial='Distrimay',
            email='contact@example.com',
            phone='1234567890',
            address='123 Main St'
        )
    def test_str_representation(self):
        self.assertEqual(str(self.proveedores), '123 Distrimay')
    def test_NIT_max_length(self):
        self.assertLessEqual(len(self.proveedores.NIT), 50)
    def test_email_validity(self):
        self.assertTrue('@' in self.proveedores.email)
    def test_phone_max_length(self):
        self.assertEqual(len(self.proveedores.phone), 10)