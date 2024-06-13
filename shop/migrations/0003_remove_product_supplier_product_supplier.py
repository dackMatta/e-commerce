# Generated by Django 5.0.3 on 2024-06-05 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_supplier_rename_category_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ManyToManyField(to='shop.supplier'),
        ),
    ]
