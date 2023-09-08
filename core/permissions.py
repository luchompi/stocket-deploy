from rest_framework.permissions import BasePermission

class isLogged(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
class isAdminOrSuperuser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.is_staff or request.user.groups.filter(name__in='Administrador').exists()

class isEncargado(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in='Encargado').exists()
