# Generated by Django 3.2.7 on 2021-09-18 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='chat_id',
            field=models.IntegerField(unique=True, verbose_name='Telegram chat id'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_uuid',
            field=models.UUIDField(primary_key=True, serialize=False, verbose_name='Customer uuid'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=15, unique=True, verbose_name='Customer phone'),
        ),
    ]
