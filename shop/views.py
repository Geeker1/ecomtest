from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,SubCategory,Product
from cart.forms import CartAddProductForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .recommender import Recommender #imports the recommendation algorithm engine coded
# Create your views here.




def home(request):
    categories = Category.objects.all()
    hot = Product.objects.all()[:8]
    feat = Product.objects.all()[:4]
    sub_category = SubCategory.objects.all()

    cart_product_form = CartAddProductForm
    return render(request, 'shop/ecom.html', {'categories':categories,
    'hot':hot,
    'feat':feat,
    'cart_product_form':cart_product_form})




def category(request,category_slug=None, sub_category_slug=None):
    category = None
    products = Product.objects.all()
    sub_category = SubCategory.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        sub_category = sub_category.filter(category=category, slug=sub_category_slug)
        products = products.filter(available=True)
        cart_product_form = CartAddProductForm
    

    return render(request,
    'shop/category.html',
    {'category':category,
    'sub_category':sub_category,
    'products':products,'cart_product_form':cart_product_form})




def sub_category(request,category_slug=None, sub_category_slug=None):
    category = None
    sub_category = None
    products = Product.objects.all()
    if sub_category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        sub_category = get_object_or_404(SubCategory, slug=sub_category_slug)
        products = products.filter(sub_category=sub_category)
        cart_product_form = CartAddProductForm
    return render(request,
    'shop/sub_category.html',
    {'category':category,
    'sub_category':sub_category,
    'products':products, 'cart_product_form':cart_product_form})



def product_detail(request, id,slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request, 'shop/product_detail.html', 
    {'product':product,
    'cart_product_form': cart_product_form,
    'recommended_products': recommended_products})

