from django.urls import path as p
from rest_framework.urlpatterns import format_suffix_patterns as fsp

from . import views as v

urlpatterns = [
	# APIS de funcionarios
	p('funcionarios/', v.FuncionarioIndex.as_view()),
	p('funcionarios/<str:pk>/', v.FuncionarioDetail.as_view()),
	p('funcionarios/search/<str:pk>/', v.FuncionarioSearch.as_view()),
	# APIS de proveedores
	p('proveedores/', v.ProveedoresIndex.as_view()),
	p('proveedores/<str:pk>/', v.ProveedoresDetail.as_view()),
	p('proveedores/search/<str:pk>/', v.SearchProveedor.as_view()),
]

urlpatterns = fsp(urlpatterns)
