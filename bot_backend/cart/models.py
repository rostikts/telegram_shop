from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import Product
from customer.models import Customer


class Cart(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    checked_out = models.BooleanField(default=False)


class CartItem(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


@receiver(post_save, sender=CartItem)
def cart_price_handler(sender: CartItem, instance: CartItem, **kwargs):
    all_items = CartItem.objects.filter(cart=instance.cart).all()
    instance.cart.total_price = 0
    for item in all_items:
        instance.cart.total_price += item.quantity * item.product.price
    instance.cart.save()