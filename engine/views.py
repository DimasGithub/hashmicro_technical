from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from engine.models import Module
from engine.handlers import ModuleHandlers, ModuleException
from django.contrib.auth.decorators import login_required
from django.core.management import call_command

# Create your views here.
def list_module(request, template_name="engine/module_list.html"):
  context = {}
  modules = Module.objects.filter(deleted_at__isnull=True)
  context['modules'] = modules
  return render(request, template_name, context)

@login_required(login_url='login')
def install_module(request, module_id):
  try:
    module_object = get_object_or_404(Module, module_id=module_id)
    if request.user.is_superuser:
      module = ModuleHandlers(module_object)
      module.install()
      messages.success(request, f"The Module {module_object.name} installed successfully.")
    else:
      messages.error(request, f"The Module can install only superuser access accounts.")
  except ModuleException as err:
    messages.error(request, f"Occurs Error : {err}")
  return redirect('module:list_module')

@login_required(login_url='login')
def upgrade_module(request, module_id):
  try:
    module_object = get_object_or_404(Module, module_id=module_id)
    previous_version = module_object.version
    if request.user.is_superuser:
      module = ModuleHandlers(module_object)
      new = module.upgrade()
      if previous_version < new.version:
        messages.success(request, f"The Module {module_object.name} upgraded successfully.")
      else:
        messages.warning(request, f"The Module {module_object.name} no upgrade detected.")
    else:
      messages.error(request, f"The Module can install only superuser access accounts.")
  
  except ModuleException as err:
    messages.error(request, f"Occurs Error : {err}")
  
  return redirect('module:list_module') 

@login_required(login_url='login')
def uninstall_module(request, module_id):
  try:
    module_object = get_object_or_404(Module, module_id=module_id)
    if request.user.is_superuser:
      module = ModuleHandlers(module_object)
      module.uninstall()
      messages.success(request, f"The Module {module_object.name} uninstalled successfully.")
    else:
      messages.error(request, f"The Module can uninstall only superuser access accounts.")
  except ModuleException as err:
    messages.error(request, f"Occurs Error : {err}")
  return redirect('module:list_module')
  

