# Generated by Django 4.0.5 on 2022-06-30 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0010_loansrepaymentbase_nok'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loansrepaymentbase',
            name='nok',
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='nok_Relationship',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='nok_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='nok_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='nok_phone_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
