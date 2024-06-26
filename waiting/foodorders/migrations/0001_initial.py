# Generated by Django 4.2.13 on 2024-06-26 15:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foodorders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foodorders', to='account.account')),
            ],
            options={
                'db_table': 'foodorders',
            },
        ),
        migrations.CreateModel(
            name='FoodordersItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foodorders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foodorder_items', to='foodorders.foodorders')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food')),
            ],
            options={
                'db_table': 'foodorders_item',
            },
        ),
    ]
