import io
from engine.models import Module
from django.core.management import call_command
class ModuleException(Exception):
    pass

class ModuleHandlers():
  object: Module
  NO_CHANGE_DB = "no_changes_detected"
  NO_MIGRATE_DB = "no_migrations_to_apply"

  def __init__(self, object):
    if not object:
      raise self.ModuleException('Model is Null.')    
    self.object = object

  def __check(self):
    if self.object.deleted_at:
      raise ModuleException('Model was deleted')

  def install(self) -> Module:
    self.__check()

    if self.object.installed:
      raise ModuleException('Model was installed.')
    
    self.object.installed = True
    self.object.save()
    
    return self.object

  def _read_output(self, stream: io.StringIO) -> str:
    try:
      res = stream.getvalue().strip().replace(" ", "_").lower()    
      return res
    finally:
      stream.close()

  def _run_command(self, command: str) -> str:
    stream = io.StringIO()
    call_command(command, stdout=stream)
    return self._read_output(stream)

  def _makemigrations_cmd(self) -> bool:
    r = self._run_command('makemigrations')
    print("s ds_ ", r)
    return r != self.NO_CHANGE_DB

  def _migrate_cmd(self) -> bool:
    r =self._run_command('migrate')
    print("->>>>_ ", r)
    return r != self.NO_MIGRATE_DB

  def _execute_cmd(self) -> bool:
    return all([self._makemigrations_cmd(), self._migrate_cmd()])

  def upgrade(self) -> Module :
    self.__check()
    if self.object.installed is False:
      raise ModuleException('Model not founded.')

    #call command
    cmd = self._execute_cmd()
    if cmd:
      self.object.version += 1
      self.object.save()
    return self.object
    
  def uninstall(self) -> Module:
    self.__check()
    if self.object.installed is False:
      raise ModuleException('Model was uninstalled.')

    self.object.installed = False 
    self.object.save()

    return self.object