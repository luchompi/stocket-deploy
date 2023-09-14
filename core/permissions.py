from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

def admin_required(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return func(self, request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    return wrapper

def admin_or_superuser_required(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        usuario = request.user
        user_groups = usuario.groups.all()
        if request.user.is_superuser or user_groups.filter(name='Administrador').exists():
            return func(self, request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    return wrapper

def admin_or_superuser_or_encargado_required(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        usuario = request.user
        user_groups = usuario.groups.all()
        if request.user.is_superuser or user_groups.filter(name='Administrador').exists() or user_groups.filter(name='Encargado').exists():
            return func(self, request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    return wrapper

def login_required(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        usuario = request.user
        if request.user.is_authenticated:
            return func(self, request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    return wrapper