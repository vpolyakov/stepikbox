from django.db import models

from items.models import Item
from users.models import User


class Cart(models.Model):
    items = models.ManyToManyField(Item, through='CartItem', related_name='carts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_detail')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='citems')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
