from django.shortcuts import render
from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from .models import Product
# from django.views import product_list_view


# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/products_list.html'
    
    # def get(self,request,*args,**kwargs):
    #     context = {
    #     "object_list": self.queryset
    #     }
    #     return render(request ,self.template_name,context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
     
    context=  {'category': category,
                'categories': categories,
                'products': products
                }

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        return render(request,'products/products_list.html', {context})

# def product_detail(request, id,slug):
#     product = get_objecet_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     context={'product':product,
#              'cart_product_form': cart_product_form}
#     return render(request,'shop/product/detail.html',{context})

# def product_create_view(request):
#     form=ProductForm(request.POST or None)
#     #if request.method=="POST":
#     if form.is_valid():
#         form.save()
#         form=ProductForm
#     context = {
#         'form':form
#     }
#     return render(request,"product_create.html", context )

# -----PRODUCT---DETAIL----VIEW 

# class ProductDetailView(DetailView):
#      queryset =  Product.objects.all()
#      template_name = 'products/products_detail.html'      

# def product_detail_view(request): 
#     obj=Product.objects.get(id=1)
#     #obj=Product.objects.create(**cleaned_data)
#     # context={
#     #     "title":obj.title,
#     #     "description":obj.description 
#     context={
#         'object':obj
#     }
#     return render(request,"products/product_detail.html",context)

# def dynamic_lookup_view(request, my_id):
#     obj=Product.objects.get(id=my_id)
#     obj=get_object_or_404(Product, id=my_id)
#     context={
#         "object" : obj
#     }
#     return render(request,"detail.html",context)