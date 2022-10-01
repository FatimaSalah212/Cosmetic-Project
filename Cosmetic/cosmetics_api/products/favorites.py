from Account.authorization import GlobalAuth
from Cosmetic.models import *
from Cosmetic.schemas import FavoriteOut, IsFavorite, MessageOut
from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

Favorite_Router = Router(tags=['Favorite'])


@Favorite_Router.get(f"/list_favorite", response={
    200: List[FavoriteOut],
    404: MessageOut
}, auth=GlobalAuth())
def list_favorite(request):
    user = User.objects.get(id=request.auth['pk'])
    favorites = Favorite.objects.filter(user=user)
    if not favorites:
        return 404, {'detail': 'No favorites found'}
    return favorites


@Favorite_Router.post(f"/add_favorite", response={
    200: MessageOut,
    400: MessageOut

}, auth=GlobalAuth())
def add_favorite(request, product_id: int):
    user = User.objects.get(id=request.auth['pk'])
    fa = user.favorites.all().filter(product_id=product_id)
    if fa:
        return 400, {'detail': f'Product with id {product_id} was in favorite'}

    favorite_in = Favorite.objects.create(product_id=product_id, user=user)
    favorite_in.save()
    return 200, {'detail': f'Product with id {product_id} add to favorite'}


@Favorite_Router.delete(f"/Remove_favorite", response={
    200: MessageOut,
    404: MessageOut
}, auth=GlobalAuth())
def remove_favorite(request, product_id: int):
    user = User.objects.get(id=request.auth['pk'])
    fa = user.favorites.all().filter(product_id=product_id)
    if fa:
        fa = get_object_or_404(Favorite, product_id=product_id, user=user)
        fa.delete()
        return 200, {'detail': f'Product with id {product_id} remove from favorite'}
    return 404, {'detail': f'Product with id {product_id} was not in favorite'}


@Favorite_Router.get("is_favorites", response={
    200: IsFavorite,
    400: IsFavorite
}, auth=GlobalAuth())
def is_favorites(request, product_id: int):
    try:
        product = Favorite.objects.get(product_id=product_id, user=User.objects.get(id=request.auth['pk']))
        if product:
            return 200, {'is_favorite': 'True'}
    except Favorite.DoesNotExist:
        return 200, {'is_favorite': 'False'}
