from Cosmetic.models import Product
from Cosmetic.schemas import ProductOut, MessageOut
from django.db.models import Q
from ninja import Router
from typing import List
from django.contrib.auth import get_user_model

User = get_user_model()

Product_Router = Router(tags=['Product'])


@Product_Router.get("/list-products", response={
    200: List[ProductOut],
    404: MessageOut
})
def all_products(request, *,
                 query: str = None,
                 price_from: int = None,
                 price_to: int = None,
                 ascending: str = None,
                 descending: str = None,
                 abc: str = None,
                 cba: str = None,
                 ):
    products = Product.objects.filter(is_active=True).order_by('brand').select_related('category', 'brand')
    if not products:
        return 404, {'detail': 'No Products found'}
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(brand__brand_name__icontains=query)
        )

    if price_from:
        products = products.filter(price__gte=price_from)

    if price_to:
        products = products.filter(price__lte=price_to)

    if ascending:
        products = products.order_by('price')

    if descending:
        products = products.order_by('-price')
    if abc:
        products = products.order_by('name')

    if cba:
        products = products.order_by('-name')

    return products


@Product_Router.get(f"/products", response={
    200: List[ProductOut],
    404: MessageOut
})
def product(request, product_id: int):
    products = Product.objects.filter(id=product_id).select_related('category', 'brand')
    if not products:
        return 404, {'detail': f'Product with id {product_id} does not exist'}
    return products
