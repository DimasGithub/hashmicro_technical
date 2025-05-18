import uuid
from django.db import models
from hashapp.model_base import TimeStampedModel
from django.urls import reverse

class Product(TimeStampedModel):
  name = models.CharField(max_length=255)
  barcode = models.UUIDField(max_length=255, primary_key=True, default = uuid.uuid4, editable=False)
  price = models.FloatField(default=0.0)
  stock = models.BigIntegerField(default=0)

  def save(self, **kwargs):
    if self.barcode is None: 
      self.barcode = uuid.uuid4()
    super().save(**kwargs)
  
  @property
  def img_barcode(self, **kwargs):
    if self.barcode is None: image_barcode = uuid.uuid4()
    image_barcode = self.barcode
    url_barcode = f"https://barcode.orcascan.com/?type=code128&data={image_barcode}"
    return url_barcode

  @property
  def get_delete_url(self):
      return reverse('module_contoh:delete_product', kwargs={'barcode': self.barcode})

  def __str__(self):
    return f"{self.name}"

  class Meta:
    db_table = 'product'
    verbose_name = 'Product'
    verbose_name_plural = 'Products'
    ordering = ['-created_at']
    


  