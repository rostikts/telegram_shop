from django.db import models


class Customer(models.Model):
    customer_uuid = models.UUIDField(verbose_name='Customer uuid', primary_key=True)
    phone = models.CharField(verbose_name='Customer phone', max_length=15, unique=True)
    chat_id = models.IntegerField(verbose_name='Telegram chat id', unique=True)
