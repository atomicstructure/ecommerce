from django.db import models
from account.models import Account
from store.models import Products, Variation
# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    # For cart item
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        # For sub total of cart item
        return self.product.price * self.quantity

    def __str__(self):
        return str(self.product)