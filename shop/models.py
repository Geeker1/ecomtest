from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100,
    db_index = True)
    slug = models.SlugField(max_length = 200, db_index = True)
    urlimage = models.URLField(max_length=250, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category',
        args=[self.slug])




class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='sub_categories')
    name = models.CharField(max_length=100,
    db_index = True)
    slug = models.SlugField(max_length = 200, db_index = True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    urlimage = models.URLField(max_length=250, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sub_category',
        args=[self.slug])

class Product(models.Model):
    procat = models.ForeignKey(Category, related_name='procats', blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, related_name='products')
    name = models.CharField(max_length=200, db_index = True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slashed = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    urlimage = models.URLField(max_length=350,blank=True, null=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)
        #This specifies index for id and slug and is deined to query products 
        #by both id and slug

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',
        args=[self.id,self.slug])



''' 
The category variable is a many to one relationship.... a product belongs 
to one category and a category has multiple products products
SLUG: This is held to build beatiful urls

'''