# Generated by Django 3.2.7 on 2021-09-20 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='customer_id',
            new_name='customer',
        ),
    ]
