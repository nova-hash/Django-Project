from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from myapp.models import product


def addproducts(request):
    return render(request,"add_product.html")

def insertproduct(request):
    if request.method == "POST":
        name = request.POST.get("pname")
        price = request.POST.get("pprice")
        desc = request.POST.get("pdesc")
        image = request.FILEs["pimage"]

        query = product(productname=name,productprice=price,productdesc=desc,productimage=image)
        query.save()
        messages.success(request,"ADD PRODUCT SUCCESSFULLY")
    else:
        pass

    return render(request,"add_product.html")





