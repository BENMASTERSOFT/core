# Generated by Django 4.0.5 on 2022-07-12 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0040_commodity_loan_upload_transaction_header_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity_loan_upload_transaction_header',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperative.commodity_categories'),
        ),
    ]
