from django.db import models
from products.models import Product
from users.models import User


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
