# Generated by Django 4.2.4 on 2023-09-06 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_order_product_shippingaddress_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]