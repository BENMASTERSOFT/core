# Generated by Django 3.2.8 on 2022-02-02 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0096_rename_amount_monthlyoverdeductionsrefund_over_deduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlydeductionlistgeneratedcertified',
            name='refund_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='cooperative.processingstatus'),
        ),
    ]
