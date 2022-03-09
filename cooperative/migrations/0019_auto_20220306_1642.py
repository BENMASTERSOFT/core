# Generated by Django 3.2.8 on 2022-03-06 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0018_members_commodity_loan_application_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='members_commodity_loan_application_temp',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperative.commodity_period_batch'),
        ),
        migrations.AddField(
            model_name='members_commodity_loan_application_temp',
            name='period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperative.commodity_period'),
        ),
    ]
