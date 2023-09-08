from django.apps import AppConfig


class EmpresaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Empresa'

    def ready(self) -> None:
        from .signals import limitar_registros_empresa

