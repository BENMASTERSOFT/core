# Generated by Django 4.0.5 on 2022-08-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0111_members_commodity_loan_application_loan_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlydeductionlistgenerated',
            name='rectified',
            field=models.CharField(choices=[('NO', 'NO'), ('YES', 'YES')], default='NO', max_length=20),
        ),
    ]