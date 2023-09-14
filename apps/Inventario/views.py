from core.permissions import admin_or_superuser_or_encargado_required
from django.db import transaction
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Marca, Categoria, Referencia, Elemento
from .serializers import CategoriaSerializer, MarcaSerializer, ReferenciaStoreSerializer, ReferenciaSerializer, \
	ElementoSerializerPreview, ElementoSerializer, ElementoViewSerializer


# Controladores de marcas
class MarcaSearch(APIView):
    @admin_or_superuser_or_encargado_required
    def get(self, request, pk, format=None):
        queryset = Marca.objects.filter(name__icontains=pk)
        serializer = MarcaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MarcaIndex(APIView):
    @admin_or_superuser_or_encargado_required
    def get(self, request, format=None):
        queryset = Marca.objects.order_by('-created_at')[:5]
        serializer = MarcaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @admin_or_superuser_or_encargado_required
    def post(self, request, format=None):
        serializer = MarcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarcaDetail(APIView):
    @admin_or_superuser_or_encargado_required
    def get(self, request, id, format=None):
        queryset = get_object_or_404(Marca, pk=id)
        serializer = MarcaSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @admin_or_superuser_or_encargado_required
    def put(self, request, id, format=None):
        marca = get_object_or_404(Marca, pk=id)
        serializer = MarcaSerializer(marca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @admin_or_superuser_or_encargado_required
    def delete(self, request, id, format=None):
        marca = get_object_or_404(Marca, pk=id)
        marca.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# controladores de Categorias
class CategoriaIndex(APIView):
    @admin_or_superuser_or_encargado_required
    def get(self, request, format=None):
        queryset = Categoria.objects.order_by('-created_at')[:5]
        serializer = CategoriaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @admin_or_superuser_or_encargado_required
    def post(self, request, format=None):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaSearch(APIView):
    @admin_or_superuser_or_encargado_required
    def get(self, request, pk, format=None):
        queryset = Categoria.objects.filter(name__icontains=pk)
        serializer = CategoriaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoriaDetail(APIView):
    @admin_or_superuser_or_encargado_required
    def delete(self, request, pk, format=None):
        queryset = get_object_or_404(Categoria, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @admin_or_superuser_or_encargado_required
    def put(self, request, pk, format=None):
        queryset = get_object_or_404(Categoria, pk=pk)
        serializer = CategoriaSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @admin_or_superuser_or_encargado_required
    def get(self, request, pk, format=None):
        queryset = get_object_or_404(Categoria, pk=pk)
        serializer = CategoriaSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Referencias Controller
class ReferenciaIndex(APIView):
    @admin_or_superuser_or_encargado_required
    def get(self, request, pk, format=None):
        queryset = Referencia.objects.filter(categoria__id=pk).order_by('-timestamps')[:5]
        serializer = ReferenciaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @admin_or_superuser_or_encargado_required
    def post(self, request, pk, format=None):
        data_list = request.data
        try:
            with transaction.atomic():
                for data in data_list:
                    myData = {
                        'categoria': pk,
                        'marca': data['id']
                    }
                    serializer = ReferenciaStoreSerializer(data=myData)
                    if serializer.is_valid():
                        serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            transaction.rollback()
            return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)


class ReferenciaDetail(APIView):
    @admin_or_superuser_or_encargado_required
    def delete(self, request, pk, format=None):
        queryset = get_object_or_404(Referencia, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReferenciaFilter(APIView):
    @admin_or_superuser_or_encargado_required

    def get(self, request, marca, categoria, format=None):
        queryset = get_list_or_404(Referencia, categoria__name=categoria, marca__name__icontains=marca)
        serializer = ReferenciaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Elemento controller
class ElementoIndex(APIView):
    @admin_or_superuser_or_encargado_required

    def get(self, request, format=None):
        queryset = Elemento.objects.order_by('-created_at')[:5]
        serializer = ElementoSerializerPreview(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ElementoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ElementoSearch(APIView):
    @admin_or_superuser_or_encargado_required

    def get(self, request, pk, format=None):
        queryset = Elemento.objects.filter(placa__icontains=pk)
        serializer = ElementoSerializerPreview(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ElementoDetail(APIView):
    @admin_or_superuser_or_encargado_required

    def get(self, request, pk, format=None):
        queryset = get_object_or_404(Elemento, placa=pk)
        serializer = ElementoViewSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        queryset = get_object_or_404(Elemento, placa=pk)
        serializer = ElementoSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ElementoABaja(APIView):
    @admin_or_superuser_or_encargado_required

    def put(self, request, pk, format=None):
        q = Elemento.objects.get(placa=pk)
        q.estado = 'Para baja'
        q.save()
        return Response(status=status.HTTP_200_OK)
