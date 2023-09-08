from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import JsonResponse
from .models import Empresa

@receiver(pre_save, sender=Empresa)
def limitar_registros_empresa(sender,instance,**kwargs):
    if Empresa.objects.count() == 1:
        response_data = {
            'error': 'Ya existe un registro en la tabla Empresa. No puedes crear más registros.'
        }
        return JsonResponse(response_data, status=400)
    