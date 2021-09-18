from django.db import models


class Customer(models.Model):
    customer_uuid = models.UUIDField(verbose_name='Customer uuid')
    phone = models.CharField(verbose_name='Customer phone', max_length=11)
    chat_id = models.IntegerField(verbose_name='Telegram chat id')
