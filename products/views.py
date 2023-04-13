from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreateProduct
from django.contrib import messages
from .models import Product
# Create your views here.

@login_required
def c_product(request,pk):
    user=User.objects.get(id=pk)
    form=CreateProduct(initial={'owner':user})
    if request.method=='POST':
        form=CreateProduct(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,  'The product has been created successfully.')
            return redirect('home')
    print('form',form)
    context={
        'form':form
            }
            
    return render(request,'products/create.html',context)


@login_required
def u_product(request,pk):
    product=Product.objects.get(id=pk)
    form=CreateProduct(instance=product)
    if request.method=='POST':
        form=CreateProduct(request.POST,instance=Product.objects.get(id=pk))
        if form.is_valid():
            form.save()
            messages.success(request,  'The product has been updated successfully.')
            return redirect('home')
    print('form',form)
    context={
        'form':form,
        'product':product
            }
            
    return render(request,'products/update.html',context)

def list_products(request):
    products=Product.objects.all()
    context={
        'products':list(products)
    }
    return render(request,'products/home.html',context)
   

@login_required
def delete_product(request,pk):
    product=Product.objects.get(id=pk)
    context={
        'product':product
            }
    if request.method=='POST': 
      product.delete()
      messages.success(request,  'The product has been deleted successfully.')
      return redirect('home')
   
            
    return render(request,'products/delete.html',context)

@login_required
def list_product(request,pk):
    product=Product.objects.get(id=pk)
    context={
        'product':product
    }
    return render(request,'products/list.html',context)
   