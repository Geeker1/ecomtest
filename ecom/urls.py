"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, static,include
from django.contrib import admin
import cart
from shop import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from sendmail import views as send_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sendmail/', include('sendmail.urls',namespace='sendmail',app_name='sendmail')),
    url(r'^blog/', include('blog.urls',namespace='blog',app_name='blog')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^coupons/',include('coupons.urls', namespace='coupons')),
    url(r'^$', views.home, name='home' ),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(
        template_name='login.html'),  name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contact_save/$', views.contact_save, name='contact_save'),
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view
        (template_name='password_reset.html',
         email_template_name='password_reset_email.html',
         subject_template_name='password_reset_subject.txt'
         ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'
        ),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'),name='password_reset_complete'
        ),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.category, name='category'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<sub_category_slug>[-\w]+)/$', views.sub_category, name='sub_category'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)



