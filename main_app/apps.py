"""Config for main_app"""

from django.apps import AppConfig


class MainAppConfig(AppConfig):
    """Class with config for main_app"""
    default_auto_field = "django.db.models.BigAutoField"
    name = "main_app"
