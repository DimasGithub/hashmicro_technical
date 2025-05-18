from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from module_contoh.models import Product
from datetime import datetime
from module_contoh.form import ProductForm

# Create your views here.
def list_product(request, template_name="module_contoh/product_list.html"):
  context = {}
  products = Product.objects.filter(deleted_at__isnull=True)
  context['products'] = products
  return render(request, template_name, context)

@login_required(login_url="login")
def delete_product(request, barcode):
  try:
    if not request.user.has_perm('module_contoh.delete_product'):
       messages.error(request, "Limited access, your account has action restrictions. Delete data unsuccessfully!")
       return redirect('module_contoh:list_product')
    product: Product = get_object_or_404(Product, barcode=barcode).delete()
    messages.success(request, "Product deleted successfully!")
  except Exception as err:
    messages.error(request, "Occurs request failed.")
  return redirect('module_contoh:list_product')

@login_required(login_url="login")
def create_product(request):
    try:
      form = ProductForm(request.POST or None)
      if request.method == 'POST' and form.is_valid():
          if not request.user.has_perm('module_contoh.add_product'):
            print(request.user.get_all_permissions())
            messages.error(request, "Limited access, your account has action restrictions. Create data unsuccessfully!")
          else:
            form.save()
            messages.success(request, "Product created successfully!")
          return redirect('module_contoh:list_product')

      return render(request, 'module_contoh/form_product.html', {
          'form': form,
          'mode':'Create'
      })
    except Exception as err:
      messages.error(request, f"Occurs request failed : {err}.")
    
    return redirect('module_contoh:list_product')

@login_required(login_url="login")
def edit_product(request, barcode):
    try:
      product = get_object_or_404(Product, barcode=barcode)
      form = ProductForm(request.POST or None, instance=product)
      if request.method == 'POST' and form.is_valid():
          if not request.user.has_perm('module_contoh.change_product'):
            messages.error(request, "Limited access, your account has action restrictions. Delete data unsuccessfully!")
          else:
            form.save()
            messages.success(request, "Product updated successfully!")
          return redirect('module_contoh:list_product')

      return render(request, 'module_contoh/form_product.html', {
          'form': form,
          'product': product,
          'mode':'Update'
      })
    except Exception as err:
      messages.error(request, f"Occurs request failed : {err}.")
    
    return redirect('module_contoh:list_product')
    



