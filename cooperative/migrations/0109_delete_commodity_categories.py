# Generated by Django 3.2.8 on 2022-02-07 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0108_alter_commodity_categories_receipt_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Commodity_Categories',
        ),
    ]
