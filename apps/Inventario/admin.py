from django.contrib import admin
from .models import Marca, Categoria, Referencia, Elemento

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Referencia)
admin.site.register(Elemento)