# Generated by Django 4.0.5 on 2022-08-23 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0113_loansrepaymentbase_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='members_commodity_loan_completed_transactions',
            name='phone_no1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='members_commodity_loan_completed_transactions',
            name='phone_no2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
