# Generated by Django 3.2.8 on 2022-03-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0009_commodity_product_list_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity_product_list',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commodity_product_list',
            name='product_model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
