# Generated by Django 4.0.5 on 2022-07-01 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0016_rename_transaction_commodity_category_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity_category_sub',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='INACTIVE', max_length=20),
        ),
    ]