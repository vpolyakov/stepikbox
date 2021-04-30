from rest_framework import serializers

from carts.models import Cart, CartItem
from items.serializers import ItemSerializer


class CartItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    total_price = serializers.SerializerMethodField()
    item_id = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'item', 'item_id', 'quantity', 'price', 'total_price']

    def get_total_price(self, obj):
        return f'{obj.quantity * obj.price:.2f}'

    def get_item_id(self, obj):
        return str(obj.item.id)


class CartSerializer(serializers.ModelSerializer):
    citems = CartItemSerializer(many=True, read_only=True)
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'citems', 'total_cost']


    def get_total_cost(self, obj):
        return obj.id
