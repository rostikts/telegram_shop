# Generated by Django 3.2.7 on 2021-09-20 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0004_alter_product_product_uuid'),
        ('customer', '0002_auto_20210918_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('checked_out', models.BooleanField(default=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]