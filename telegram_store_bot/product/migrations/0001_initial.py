# Generated by Django 3.2.7 on 2021-09-18 14:53

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
                ('product_uuid', models.UUIDField(default=uuid.UUID('d7be4616-165b-424f-8f75-2ec0a7cbc311'), editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]