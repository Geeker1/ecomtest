from django.shortcuts import render,redirect

# Create your views here.

from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponApplyForm

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
            valid_from__lte=now,
            valid_to__gte=now,
            active = True)
            request.session['coupon_id'] = coupon.id

        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')



#This view tries to validate the coupon and store it in the user session
#The decorator is used to restrict this view to only post requests