# Generated by Django 5.0.6 on 2024-07-10 06:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("foodorders", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="foodordersitem",
            old_name="price",
            new_name="foodprice",
        ),
        migrations.RenameField(
            model_name="foodordersitem",
            old_name="quantity",
            new_name="foodquantity",
        ),
    ]
