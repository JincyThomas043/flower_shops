# Generated by Django 5.0.2 on 2024-03-26 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0012_remove_cart_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=15)),
                ('zip_code', models.CharField(max_length=10, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('notes', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=1)),
                ('total_price', models.IntegerField()),
                ('payment_status', models.CharField(max_length=20, null=True)),
                ('purchase_date', models.DateTimeField(auto_now=True, null=True)),
                ('product_status', models.CharField(default='Order Placed', max_length=50, null=True)),
                ('instruction', models.CharField(default='Your Order Has Been Successfully Placed', max_length=50, null=True)),
                ('product_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.productdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.registration')),
            ],
        ),
    ]
