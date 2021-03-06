# Generated by Django 3.2.7 on 2021-09-18 22:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_uuid', models.UUIDField(default=uuid.UUID('11083e36-6ab7-4810-a5be-057c85b5c241'), editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
