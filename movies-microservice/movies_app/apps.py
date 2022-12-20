from django.apps import AppConfig
from movies_project import container


class MoviesAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "movies_app"

    def ready(self):
        container.wire(modules=[".views"])
