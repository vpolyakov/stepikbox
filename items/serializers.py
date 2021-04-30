from rest_framework import serializers

from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    # price = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('id', 'title', 'description', 'image', 'weight', 'price')

    # def get_price(self, obj):
    #     return f'{obj.price:.2f}'
