# Generated by Django 4.0.5 on 2022-07-19 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0075_remove_loanapplication_approved_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanapplicationshortlisting',
            name='processing_status',
            field=models.CharField(choices=[('UNPROCESSED', 'UNPROCESSED'), ('PROCESSED', 'PROCESSED')], default='UNPROCESSED', max_length=20),
        ),
    ]
