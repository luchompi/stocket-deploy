from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns as fsp

from . import views

urlpatterns = [
    ###APIs de Asignaciones
    # Lista de asignaciones y las crea
    path('asignaciones/', views.AsignacionIndex.as_view()),
    # Filtrado de asignaciones por funcionario o id
    path('asignaciones/filter/<int:pk>/', views.AsignacionSearch.as_view()),
    # obtener una asignacion por id, traspasarla o anularla.
    path('asignaciones/details/<int:pk>/', views.AsignacionDetail.as_view()),
    # obtener elementos de una asignacion
    path('asignaciones/detalles/<int:pk>/', views.DetallesAsignacionDetail.as_view()),
    # obtener elementos disponibles para asignar
    path('asignaciones/detalles/disponibles/', views.DetalleAsignacionSearch.as_view()),
    # obetenr elementos disponibles para asignar por argumentos
    path('asignaciones/detalles/disponibles/args/', views.SearchElementByArgs.as_view()),

    ###APIS de mantenimiento
    # Lista de mantenimientos
    path('mantenimientos/', views.MantenimientoIndex.as_view()),
    # Crea un nuevo mantenimiento
    path('mantenimientos/create/<int:pk>/', views.MantenimientoCreate.as_view()),
    # Obtener detalles de un mantenimiento
    path('mantenimientos/details/<int:pk>/', views.MantenimientoDetails.as_view()),

    # Obtener elementos cuyo estado sea En mantenimiento
    path('mantenimientos/elementos/en_proceso/', views.ComprobarMantenimiento.as_view()),

    ###APIS de bajas
    # Lista de bajas
    path('bajas/', views.BajaIndex.as_view()),
    # Crea una nueva baja y añade elementos a ella
    path('bajas/elementos/', views.BajaCreate.as_view()),
    # Obtener detalles de una baja
    path('bajas/details/<int:pk>/', views.BajaDetails.as_view()),
    # Borrar baja, detalles y elementos
    path('bajas/delete/', views.BorrarRegistros.as_view()),
    ###APIS de certificacion
    # Generar certificado de asignacion
    path('certificacion/asignacion/<int:pk>/', views.certificaciones.as_view()),
]

urlpatterns = fsp(urlpatterns)
