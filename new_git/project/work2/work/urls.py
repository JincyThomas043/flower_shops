"""
URL configuration for work project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show),
    path('ind', views.home),
    path('loabhi', views.login),

    path('service',views.service),
    path('ser',views.ser),
    path('gallery',views.gallery),
    path('price',views.price),
    path('in',views.about),
    path('shop',views.shop),
    path('all',views.all),
    path('rose',views.rose),
    path('boque',views.boque),
    path('pot', views.potflowers),
    path('valentine',views.valentine),
    path('stages', views.stages),
    path('gifts',views.gifts),
    path('search',views.Search),
    path('register',views.registration),
    path('login',views.login),
    path('lowstock',views.low_stock),
    path('imagedetails/<int:d>',views.image_details),

    path('userhome',views.user_home),
    path('adminpage',views.admin_page),
    path('logout',views.logout),
    path('viewuser',views.view_user),
    path('addproduct',views.add_product),
    path('displayproduct', views.display_product),
    path('admin_order_details', views.admin_orders, name='admin_order_details'),
    path('admin_order_update/<int:d>', views.adminorderupdate),
    path('deleteproduct/<int:d>',views.delete_product),
    path('updateproduct/<int:d>',views.update_product),
    path('addcart/<int:pid>',views.add_cart),
    path('displaycart',views.display_cart),
    path('wishlist/<int:pid>', views.display_wishlist),
    path('displaywishlist', views.wishlist),
    path('removefromcart/<int:d>',views.delete_from_cart),
    path('removefromwishlist/<int:d>', views.remove_wishlist),
    path('forgot',views.forgot_password,name="forgot"),
    path('reset/<token>',views.reset_password,name='reset_password'),
    path('increment/<int:cart_id>', views.increment_quantity, name="increment_quantity"),
    path('decrement/<int:cart_id>', views.decrement_quantity, name="decrement_quantity"),
    path('details/<int:d>', views.details),
    path('pay/<int:amount>',views.pay,name='pay'),
    path('pay1/<int:amount>',views.placeorder, name='pay1'),
    path('success_page', views.success_page),
    path('user_recent_orders', views.userrecentorders, name='user_recent_orders'),
    path('checkout_cart/<int:total>',views.checkoutcart),
    path('payment_cart/<int:l>',views.payment_cart),
    path('profile', views.profile, name='profile'),
    path('update_profile', views.updateprofile),
    path('change_password', views.changepassword),
   
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
