from uuid import uuid4

from django.db import models

from category.models import Category


class Product(models.Model):
    product_uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
