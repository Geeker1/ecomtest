from django.db import models

# Create your models here.

from django.db import models 
from shop.models import Product
from decimal import Decimal 
from django.core.validators import MinValueValidator,MaxValueValidator
from coupons.models import Coupon
from decimal import Decimal
from django.core.validators import MinValueValidator,MaxValueValidator






class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon, related_name='orders',
    blank=True, null=True)
    discount = models.IntegerField(default=0, validators=[
        MinValueValidator(0),MaxValueValidator(100)
    ])

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount/Decimal('100'))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

'''
The paid boolean field is going to be used to differentiate between paid
and unpaid orders

'''