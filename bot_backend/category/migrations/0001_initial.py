# Generated by Django 3.2.7 on 2021-09-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]