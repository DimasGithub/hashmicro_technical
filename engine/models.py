from django.db import models
from hashapp.model_base import TimeStampedModel

class Module(TimeStampedModel):
  module_id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=255)
  module_name = models.CharField(max_length=255, unique=True)
  description = models.CharField(max_length=255, null=False, blank=False)
  installed = models.BooleanField(default=False)
  version = models.FloatField(default=0.0)

  def save(self, **kwargs):
    if self.name and self.version > 0.0:
       name = str(self.name).lower().strip().replace(" ", "_")
       self.module_name = f"{name}"
    super().save(**kwargs)

  def __str__(self, **kwargs):
    return f"{self.module_name}"

  class Meta:
      db_table = 'module'
      verbose_name = 'Module'
      verbose_name_plural = 'Modules'
      ordering = ['-created_at']