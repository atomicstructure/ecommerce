# Generated by Django 5.1.1 on 2024-10-04 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_cartitem_user_alter_cartitem_cart'),
        ('category', '0004_alter_category_slug'),
        ('orders', '0006_alter_orderproduct_is_ordered'),
        ('store', '0004_rename_variations_variation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
