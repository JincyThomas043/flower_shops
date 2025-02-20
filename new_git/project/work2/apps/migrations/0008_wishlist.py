# Generated by Django 5.0.2 on 2024-02-28 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.productdetails')),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.registration')),
            ],
        ),
    ]
