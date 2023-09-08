from django.contrib import admin
from .models import Asignacion, DetallesAsignacion, Mantenimiento, Baja, DetalleBaja

admin.site.register(Asignacion)
admin.site.register(DetallesAsignacion)
admin.site.register(Mantenimiento)
admin.site.register(Baja)
admin.site.register(DetalleBaja)
