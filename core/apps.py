from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self) -> None:
        import core.signals
        return super().ready()