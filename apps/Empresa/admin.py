from django.contrib import admin
from .models import Empresa, Sede, Dependencia, SedeDependencia

admin.site.register(Empresa)
admin.site.register(Sede)
admin.site.register(Dependencia)
admin.site.register(SedeDependencia)
