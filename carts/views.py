from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from carts.models import Cart, CartItem
from carts.serializers import CartSerializer, CartItemSerializer


class CartItemViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()  # ? разобраться с basename
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart=self.request.user.cart)


class CartViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
