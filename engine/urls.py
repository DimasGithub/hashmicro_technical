from django.urls import path
from engine.views import list_module, install_module, uninstall_module, upgrade_module


app_name="module"
urlpatterns = [
  path('', list_module, name="list_module"),
  path('install/<int:module_id>', install_module, name="install_module"),
  path('upgrade/<int:module_id>', upgrade_module, name="upgrade_module"),
  path('uninstall/<int:module_id>', uninstall_module, name="uninstall_module"),
]