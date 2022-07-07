# Generated by Django 4.0.5 on 2022-07-04 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0024_alter_accountdeductions_transaction_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdeductions',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='failedloanpenaltyrecords',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlydeductiongenerationheading',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlydeductionlist',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlydeductionlistgenerated',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlygeneratedtransactions',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlygroupgeneratedtransactions',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlyjointdeductiongenerated',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlyjointdeductiongeneratedtransactions',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlyjointdeductionlist',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlyshopdeductionlist',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlyshopdeductionlistgenerated',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monthlyshopgroupgeneratedtransactions',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonmemberaccountdeductions',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
    ]