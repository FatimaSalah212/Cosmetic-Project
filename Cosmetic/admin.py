from django.contrib import admin
from Cosmetic.models import *
from Account.models import *

admin.site.register(Brand)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'discounted_price', 'category', 'brand', 'is_active', 'created']
    search_fields = ['name', 'price', 'discounted_price']
    list_filter = ['is_active']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'item_qty', 'ordered', 'checked']
    search_fields = ['user', 'product']
    list_filter = ['ordered', 'checked']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'is_active']
    search_fields = ['name', 'parent']
    list_filter = ['is_active']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total', 'status', 'checked']
    search_fields = ['user', 'product', 'status']
    list_filter = ['checked', 'status']


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product_id', 'rate', 'created']
    search_fields = ['user', 'product']
    list_filter = ['created', 'updated']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'last_login']
    search_fields = ['first_name', 'last_name']
    list_filter = ['is_staff', 'is_superuser']


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product_id']
    search_fields = ['user', 'product']
