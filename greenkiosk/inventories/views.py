
from .forms import ProductUploadForm
from .models import Product  
from django.shortcuts import render,redirect


# Create your views here.
def product_upload_view(request):
    form=ProductUploadForm()
    return render(request,"inventories/product_upload.html",{"form":form})

def products_list_view(request):
    products= Product.objects.all()
    return render(request, "inventories/products_list.html",{"products":products})

def product_detail(request,id):
    product= Product.objects.get(id=id)
    return render(request,"inventories/product_detail.html",{"product":product})

def product_update_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail", id=product.id)
    else:
        form = ProductUploadForm(instance=product)
    return render(request, "inventories/edit_product.html", {'form': form})

def delet_product(request, id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect("product_list_view")