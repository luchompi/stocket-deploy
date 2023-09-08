
import pytest
from django.core.exceptions import ValidationError
from .models import Empresa, Sede, Dependencia, SedeDependencia

@pytest.mark.django_db
def test_empresa_creation():
    empresa = Empresa.objects.create(
        NIT='123456789',
        name='Mi Empresa',
        address='Calle Principal 123',
        phone='1234567890',
        email='info@miempresa.com',
        description='Descripción de la empresa',
        web='www.miempresa.com'
    )

    assert empresa.NIT == '123456789'
    assert empresa.name == 'Mi Empresa'
    assert empresa.address == 'Calle Principal 123'
    assert empresa.phone == '1234567890'
    assert empresa.email == 'info@miempresa.com'
    assert empresa.description == 'Descripción de la empresa'
    assert empresa.web == 'www.miempresa.com'

@pytest.mark.django_db
def test_sede_creation():
    empresa = Empresa.objects.create(
        NIT='123456789',
        name='Mi Empresa',
        address='Calle Principal 123',
        phone='1234567890',
        email='info@miempresa.com',
    )
    sede = Sede.objects.create(
        name='Sede Principal',
        address='Calle Sede 456',
        phone='0987654321',
        email='sede@miempresa.com',
        empresa=empresa
    )

    assert sede.name == 'Sede Principal'
    assert sede.address == 'Calle Sede 456'
    assert sede.phone == '0987654321'
    assert sede.email == 'sede@miempresa.com'
    assert sede.empresa == empresa

@pytest.mark.django_db
def test_dependencia_creation():
    dependencia = Dependencia.objects.create(
        name='Departamento de Ventas',
        description='Descripción del departamento de ventas',
    )

    assert dependencia.name == 'Departamento de Ventas'
    assert dependencia.description == 'Descripción del departamento de ventas'

@pytest.mark.django_db
def test_sededependencia_creation():
    empresa = Empresa.objects.create(
        NIT='123456789',
        name='Mi Empresa',
        address='Calle Principal 123',
        phone='1234567890',
        email='info@miempresa.com',
    )
    sede = Sede.objects.create(
        name='Sede Principal',
        address='Calle Sede 456',
        phone='0987654321',
        email='sede@miempresa.com',
        empresa=empresa
    )
    dependencia = Dependencia.objects.create(
        name='Departamento de Ventas',
        description='Descripción del departamento de ventas',
    )
    sede_dependencia = SedeDependencia.objects.create(
        sede=sede,
        dependencia=dependencia,
    )

    assert sede_dependencia.sede == sede
    assert sede_dependencia.dependencia == dependencia
