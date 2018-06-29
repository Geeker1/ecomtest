from django.shortcuts import render,redirect,reverse,render_to_response
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

@login_required
def order_create(request):
    cart = Cart(request)
    data = dict()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            #commit=False does not save to the database because it wants to check for coupons that are available
            data['form_is_valid'] = True
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity'])
            #clear the cart
            cart.clear()
            order_created.delay(order.id)
            form = OrderCreateForm()
            context = {'form':form}
            data['html_order_form'] = render_to_string('includes/order_create.html',
            context, request=request)
            data['url'] = reverse('orders:success_me')
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            context = {'form':form}
            data['html_order_form'] = render_to_string('includes/order_create.html',
            context, request=request)
            return JsonResponse(data)
    else:
        form = OrderCreateForm()
    return render(request,'orders/order/create.html',{'cart':cart, 'form':form})

def success_me(request):
    cart = Cart(request)
    return render(request,'orders/order/created.html',{'cart':cart})