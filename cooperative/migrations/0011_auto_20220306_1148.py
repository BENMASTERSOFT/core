# Generated by Django 3.2.8 on 2022-03-06 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0010_auto_20220306_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity_product_list',
            name='amount',
        ),
        migrations.DeleteModel(
            name='Company_Products_Prices',
        ),
    ]
