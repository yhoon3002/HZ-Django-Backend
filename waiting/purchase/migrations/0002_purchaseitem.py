# Generated by Django 5.0.6 on 2024-07-10 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("drink", "0001_initial"),
        ("food", "0001_initial"),
        ("purchase", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PurchaseItem",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("foodquantity", models.PositiveIntegerField(default=1)),
                ("foodprice", models.DecimalField(decimal_places=2, max_digits=10)),
                ("drinkquantity", models.PositiveIntegerField(default=1)),
                ("drinkprice", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "drink",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="drink.drink"
                    ),
                ),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="food.food"
                    ),
                ),
                (
                    "purchase",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchase_items",
                        to="purchase.purchase",
                    ),
                ),
            ],
            options={
                "db_table": "purchase_item",
            },
        ),
    ]