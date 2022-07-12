# Generated by Django 4.0.5 on 2022-07-12 02:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0038_rename_balance_commodity_loan_upload_transaction_details_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity_loan_upload_transaction_details',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='commodity_loan_upload_transaction_details',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]