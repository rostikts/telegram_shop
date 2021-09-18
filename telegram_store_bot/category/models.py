from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=30)
