from django.urls import path
from .views import list_product, delete_product, create_product, edit_product

app_name="module_contoh"

urlpatterns = [
  path('',list_product, name="list_product"),
  path('create-product/', create_product, name="add_product"),
  path('delete-product/<str:barcode>', delete_product, name="delete_product"),
  path('update-product/<str:barcode>', edit_product, name="change_product")
]