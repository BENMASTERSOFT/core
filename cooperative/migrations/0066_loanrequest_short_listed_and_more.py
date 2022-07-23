# Generated by Django 4.0.5 on 2022-07-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0065_transactiontypes_loan_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequest',
            name='short_listed',
            field=models.CharField(choices=[('NO', 'NO'), ('YES', 'YES')], default='NO', max_length=30),
        ),
        migrations.AddField(
            model_name='loanrequest',
            name='short_listed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]