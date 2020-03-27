from django.shortcuts import render, get_object_or_404,redirect
from .models import Product
from .forms import ProductForm, RawProductForm

# list view of products
def product_list_view(request):
    queryset=Product.objects.all()
    context = {
        "object_list": queryset # object for list view is object_lsit

    }
    return render(request,"products/product_list.html", context)
    
# delete up form
def product_delete_view(request,id):
    #obj = Product.objects.get(id=1)
    print(request)
    obj= get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'obj':obj
    }
    return render(request,"products/product_delete.html",context)


# Look up form
def product_lookup_view(request,id):
    #obj = Product.objects.get(id=1)
    obj= get_object_or_404(Product, id=id)
    context = {
        'obj':obj
    }
    return render(request,"products/product_det.html",context)

# create your product view from with vaidity.
#def product_create_view(request):
 #   initial_data={
 #       'title':"this is title from view"
 #   } 
 #  form = RawProductForm()
  #  if request.method == 'POST':
   #     form = RawProductForm(request.POST or None , initial =initial_data)
    #    if form.is_valid():
     #       print(form.cleaned_data)
      #  else:
       #     print(form.errors)
    #context = {
     #    "form": form
    #}
    #return render(request,"products/product_create.html",context)




# create your product view from model form here.
def product_create_view(request):
    
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        form=ProductForm() # rerender the form to make it blank
    context = {
       # 'title': obj.title,
       # 'description': obj.description
        'form': form
    }
    return render(request,"products/product_create.html",context)

# fetch your product view here.
def product_update_view(request):
    obj = Product.objects.get(id=9)
    form= ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form=ProductForm()
    else:
        print(form.errors)
    context = {
       # 'title': obj.title,
      #  'description': obj.description
        'form': form
    }
    return render(request,"products/product_create.html",context)


# fetch your product view here.
def product_detail_view(request):
    obj = Product.objects.get(id=11)
    context = {
       # 'title': obj.title,
      #  'description': obj.description
        'obj': obj
    }
    return render(request,"products/product_det.html",context)