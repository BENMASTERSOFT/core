# Generated by Django 4.0.5 on 2022-08-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0116_members_commodity_loan_application_phone_no1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='savingsuploaded',
            name='standing_order_update',
            field=models.CharField(choices=[('NO', 'NO'), ('YES', 'YES')], default='YES', max_length=20),
        ),
    ]
