# Generated by Django 4.2.4 on 2023-09-29 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0025_shippingaddress_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
