# Generated by Django 5.1.1 on 2024-10-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_remove_orderproduct_is_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='is_ordered',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
