# Generated by Django 5.1.1 on 2024-10-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payer_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payer_names',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
