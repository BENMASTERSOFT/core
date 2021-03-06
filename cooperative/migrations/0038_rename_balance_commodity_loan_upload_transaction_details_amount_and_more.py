# Generated by Django 4.0.5 on 2022-07-12 01:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0037_remove_commodity_product_list_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commodity_loan_upload_transaction_details',
            old_name='balance',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='commodity_loan_upload_transaction_details',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='commodity_loan_upload_transaction_details',
            name='loan_amount',
        ),
        migrations.RemoveField(
            model_name='commodity_loan_upload_transaction_details',
            name='repayment',
        ),
        migrations.AddField(
            model_name='commodity_loan_upload_transaction_header',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='commodity_loan_upload_transaction_header',
            name='duration',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='commodity_loan_upload_transaction_header',
            name='interest_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='commodity_loan_upload_transaction_header',
            name='loan_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='commodity_loan_upload_transaction_header',
            name='repayment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='commodity_loan_upload_transaction_header',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
