# Generated by Django 5.0.2 on 2024-02-26 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_productdetails_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='username',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
