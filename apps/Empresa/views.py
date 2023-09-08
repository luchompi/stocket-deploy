from core.permissions import isAdminOrSuperuser, isEncargado
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Dependencia, Empresa, Sede, SedeDependencia
from .serializers import DependenciaSerializer, EmpresaSerializer, SedeDependenciaSerializer, SedeSerializer
from django.db import transaction
from django.db.models import Q

# Empresa Controllers
class EmpresaIndex(APIView):
    @permission_classes([isAdminOrSuperuser | isEncargado])
    def get(self, request, format=None):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    @permission_classes([isAdminOrSuperuser])
    def post(self, request, format=None):
        serializer = EmpresaSerializer(data=request.data)
        if Empresa.objects.count() == 1:
            return Response ({"error": "Ya existe un registro en la tabla Empresa. No puedes crear más registros."}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpresaDetails(APIView):

    @permission_classes([isAdminOrSuperuser])
    def put(self, request, pk, format=None):
        empresa = get_object_or_404(Empresa, id=pk)
        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Sede Controllers
class SedeIndex(APIView):
    @permission_classes([isAdminOrSuperuser | isEncargado])
    def get(self, request, NIT, format=None):
        sedes = get_list_or_404(Sede, empresa__NIT=NIT)
        serializer = SedeSerializer(sedes, many=True)
        return Response(serializer.data)

    @permission_classes([isAdminOrSuperuser])
    def post(self, request, NIT, format=None):
        myData = request.data.copy()
        q = Sede.objects.filter(name=myData['name'], empresa__NIT=NIT)
        if not q:
            empresa = Empresa.objects.get(NIT=NIT)
            myData['empresa'] = empresa.NIT
            serializer = SedeSerializer(data=myData)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Ya existe una sede con ese nombre."}, status=status.HTTP_400_BAD_REQUEST)

class SedeDetails(APIView):
    @permission_classes([isAdminOrSuperuser | isEncargado])
    def get(self, request, NIT, pk, format=None):
        sede = get_object_or_404(Sede, id=pk, empresa=NIT)
        serializer = SedeSerializer(sede)
        return Response(serializer.data)
    
    @permission_classes([isAdminOrSuperuser])
    def put(self, request, pk,NIT, format=None):
        sede = get_object_or_404(Sede, id=pk, empresa__NIT=NIT)
        serializer = SedeSerializer(sede, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @permission_classes([isAdminOrSuperuser])
    def delete(self, request, pk,NIT, format=None):
        try:
            sede = get_object_or_404(Sede, id=pk,empresa__NIT=NIT)
            sede.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except (sede.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

class SedeSearch(APIView):
    @permission_classes([isAdminOrSuperuser | isEncargado])
    def get(self, request, NIT, search, format=None):
        sedes = Sede.objects.filter(Q(name__icontains=search) | Q(id__icontains=search),empresa__NIT=NIT, )
        serializer = SedeSerializer(sedes, many=True)
        return Response(serializer.data)

#Dependencia controllers
class DependenciaIndex(APIView):
    @permission_classes([isAdminOrSuperuser | isEncargado])
    def get(self, request, format=None):
        sedes = Dependencia.objects.order_by('-id')[:5]
        serializer = DependenciaSerializer(sedes, many=True)
        return Response(serializer.data)

    @permission_classes([isAdminOrSuperuser])
    def post(self, request, format=None):
        serializer = DependenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DependenciaDetails(APIView):
    @permission_classes([isAdminOrSuperuser | isEncargado])
    def get(self, request, pk, format=None):
        dependencia = get_object_or_404(Dependencia, id=pk)
        serializer = DependenciaSerializer(dependencia)
        return Response(serializer.data)
    @permission_classes([isAdminOrSuperuser])
    def put(self,request,pk,format=None):
        dependencia = get_object_or_404(Dependencia, id=pk)
        serializer = DependenciaSerializer(dependencia, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @permission_classes([isAdminOrSuperuser])
    def delete(self,request,pk,format=None):
        try:
            dependencia = get_object_or_404(Dependencia, id=pk)
            dependencia.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except (dependencia.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class SearchDependencia(APIView):
    @permission_classes([isAdminOrSuperuser | isEncargado])
    def get(self, request, search, format=None):
        dependencias = Dependencia.objects.filter(Q(name__icontains=search) | Q(id__icontains=search))
        serializer = DependenciaSerializer(dependencias, many=True)
        return Response(serializer.data)
#Sedes por dependencias
class SedeByDependencia(APIView):
    @permission_classes([isAdminOrSuperuser | isEncargado])
    def get(self, request, pk, format=None):
        sedes = get_list_or_404(SedeDependencia, sede=pk)
        serializer = SedeDependenciaSerializer(sedes, many=True)
        return Response(serializer.data)
    
    @permission_classes([isAdminOrSuperuser])
    def post(self, request, pk, format=None):
        data_list = request.data['_value']
        try:
            with transaction.atomic():
                for data in data_list:
                    myData = {
                        'sede': data['sede_id'],
                        'dependencia': data['dependencia_id']
                    }    
                    serializer = SedeDependenciaSerializer(data=myData)
                    if(serializer.is_valid()):
                        serializer.save()                
                return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class SedeByDependenciaDetails(APIView):
    @permission_classes([isAdminOrSuperuser | isEncargado])
    def delete(self, request, sede_id, dep_id, format=None):
        if queryset := SedeDependencia.objects.get(id=dep_id, sede__id=sede_id):
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

class obtenerDependenciasParaSede(APIView):
    permission_classes = [isAdminOrSuperuser | isEncargado]
    def get(self, request, sede_id, format=None):
        #Consulto las dependencias que tiene la sede
        dependencias = SedeDependencia.objects.filter(sede__id=sede_id)
        #si existe una sede añadida, procedo con filtro
        if dependencias:
            #Obtengo los id de las dependencias
            ids = dependencias.values_list('dependencia', flat=True)
            #Consulto las dependencias que no estan en la sede
            dependencias = Dependencia.objects.exclude(id__in=ids)
            print(dependencias)
        else:
            dependencias = Dependencia.objects.all()
        serializer = DependenciaSerializer(dependencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)