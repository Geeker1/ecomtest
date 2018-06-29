from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from django.contrib import messages
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponse, JsonResponse
from coupons.forms import CouponApplyForm
from django.template.loader import render_to_string
import json


@require_POST
def cart_add(request,product_id):
    data = dict()
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'],update_quantity=cd['update'])
            cart = Cart(request)
            data['html_book_list'] = render_to_string('includes/partial_cart_update.html', {
                'cart': cart,'form':form
            })
            data['html_school'] = render_to_string('includes/partial_tots.html', {
                'cart': cart
            })
            data['html_remove_me'] = render_to_string('includes/partial_remove_me.html', {
                'cart': cart
            })
            data['html_sub_me'] = render_to_string('includes/partial_sub.html', {
                'cart': cart
            })
            
            data['html_coupo_me'] = render_to_string('includes/partial_coupon.html', {
                'cart': cart
            })
            data['html_mobile_me'] = render_to_string('includes/partial_mobile_me.html', {
                'cart': cart
            })

        else:
            data['form_is_invalid'] = True
            
            
    return JsonResponse(data)





def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],'update': True}
        )
         
    coupon_apply_form = CouponApplyForm()

    return render(request, 'cart/detail.html', {'cart':cart,
    'coupon_apply_form': coupon_apply_form})