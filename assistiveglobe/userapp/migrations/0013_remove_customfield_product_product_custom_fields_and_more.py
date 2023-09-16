# Generated by Django 4.2.4 on 2023-09-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0012_alter_product_category_customfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customfield',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='custom_fields',
            field=models.ManyToManyField(blank=True, to='userapp.customfield'),
        ),
        migrations.AlterField(
            model_name='customfield',
            name='value',
            field=models.CharField(max_length=255),
        ),
    ]
