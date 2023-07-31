from django.shortcuts import render
from .forms import ProductUploadForm
from .models import Product  


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