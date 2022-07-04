# Generated by Django 4.0.5 on 2022-07-03 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0019_treanding_commodity_signatory_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='loansuploaded',
            name='admin_charge_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='loansuploaded',
            name='interest_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]