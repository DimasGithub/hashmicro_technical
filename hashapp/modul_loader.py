
from django.urls import path, include
from engine.models import Module
from importlib import import_module

def get_modules_active():
    urls = []
    modules = Module.objects.filter(installed=True, deleted_at__isnull=True).values_list('module_name', flat=True)
    for module in modules:
        try:
            mod_urls = import_module(f"{module}.urls")
            module = path(f"{module}/", include(mod_urls))
            module.is_module = True
            urls.append(module)
        except ModuleNotFoundError:
            pass
    return urls





