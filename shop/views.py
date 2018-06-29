from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,SubCategory,Product
from .forms import ContactForm
from cart.forms import CartAddProductForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def contact(request):
    form = ContactForm()
    return render(request,'contact.html',{'form':form})




def contact_save(request):
    data = dict()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject,message, from_email, ['admin@frozine.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found!!')
            messages.success(request, 'You have sent the email !')
            form = ContactForm()
        else:
            data['form_is_valid'] = False
            
                
    else:
        form = ContactForm()
    
    context = {'form': form}
    data['html_contact_form'] = render_to_string('includes/contact_update.html', context, request=request)
    return JsonResponse(data)



def home(request):
    categories = Category.objects.all()
    hot = Product.objects.all()[:8]
    feat = Product.objects.all()[:4]

    cart_product_form = CartAddProductForm
    return render(request, 'ecom.html', {'categories':categories,
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
    'category.html',
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
    'sub_category.html',
    {'category':category,
    'sub_category':sub_category,
    'products':products, 'cart_product_form':cart_product_form})



def product_detail(request, id,slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product_detail.html', {'product':product,'cart_product_form': cart_product_form})



