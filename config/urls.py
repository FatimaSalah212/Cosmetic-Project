"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from ninja import NinjaAPI
from Account.authorization import GlobalAuth
from Account.account_api import account_controller
from Cosmetic.cosmetics_api.products.product import Product_Router
from Cosmetic.cosmetics_api.admin.admin import Admin_Router
from Cosmetic.cosmetics_api.products.rate import Rate_Router
from Cosmetic.cosmetics_api.order.order import Order_Router
from Cosmetic.cosmetics_api.products.favorites import Favorite_Router

api = NinjaAPI(
    title=' Pure Beauty',
    version='0.1',
    description='Our products is Crulety-free,Vegan and Eco-friendly.',
)

api.add_router('auth', account_controller)
api.add_router('Product', Product_Router)
api.add_router('Order', Order_Router, auth=GlobalAuth)
api.add_router('Rate', Rate_Router, auth=GlobalAuth)
api.add_router('Admin', Admin_Router, auth=GlobalAuth)
api.add_router('Favorite', Favorite_Router, auth=GlobalAuth)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
