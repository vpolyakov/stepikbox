from rest_framework.routers import DefaultRouter
from .views import CartItemViewSet, CartViewSet

cart_router = DefaultRouter()
cart_router.register(r'v1', CartViewSet, basename='cart')

# Не работает
cart_router.register(r'items', CartItemViewSet)  # , basename='cart_item')

urlpatterns = cart_router.urls   # + cart_item_router.urls
