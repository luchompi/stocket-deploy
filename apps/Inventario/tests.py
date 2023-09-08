# File: your_app/tests/test_models.py
import pytest
from apps.Personas.models import Proveedores
from .models import Marca, Categoria, Referencia, Elemento

@pytest.mark.django_db
def test_proveedor_model():
    Proveedores.objects.create(
        NIT="123456789",
        razonSocial="Proveedor Test",
        phone="1234567890",
        address="Test Address",
        email="test@example.com",
        city="Test City",
    )
    proveedor = Proveedores.objects.get(NIT="123456789")
    assert str(proveedor) == "123456789 Proveedor Test"

@pytest.mark.django_db
def test_marca_model():
    Marca.objects.create(
        name="Test Marca",
        description="Test Description",
    )
    marca = Marca.objects.get(name="Test Marca")
    assert str(marca) == "Test Marca"

@pytest.mark.django_db
def test_categoria_model():
    Categoria.objects.create(
        name="Test Categoria",
        description="Test Description",
    )
    categoria = Categoria.objects.get(name="Test Categoria")
    assert str(categoria) == "Test Categoria"

@pytest.mark.django_db
def test_referencia_model():
    marca = Marca.objects.create(name="Test Marca")
    categoria = Categoria.objects.create(name="Test Categoria")
    Referencia.objects.create(
        marca=marca,
        categoria=categoria,
    )
    referencia = Referencia.objects.get(marca=marca, categoria=categoria)
    assert str(referencia) == f"{marca} - {categoria}"

@pytest.mark.django_db
def test_elemento_model():
    proveedor = Proveedores.objects.create(
        NIT="123456789",
        razonSocial="Proveedor Test",
        phone="1234567890",
        address="Test Address",
        email="test@example.com",
        city="Test City",
    )
    marca = Marca.objects.create(name="Test Marca")
    categoria = Categoria.objects.create(name="Test Categoria")
    referencia = Referencia.objects.create(marca=marca, categoria=categoria)
    Elemento.objects.create(
        placa=1,
        referencia=referencia,
        serial="Test Serial",
        estado="Por asignar",
        IP="192.168.0.1",
        MAC="00:11:22:33:44:55",
        proveedor=proveedor,
        created_by="admin",
    )
    elemento = Elemento.objects.get(serial="Test Serial")
    assert str(elemento) == f"{elemento.placa} - {elemento.referencia} - {elemento.estado}"
