# Generated by Django 4.0.5 on 2022-08-26 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0119_personalledgerwithoutbalancebf'),
    ]

    operations = [
        migrations.AddField(
            model_name='wrongfuldeductiontransfer',
            name='transaction_period',
            field=models.DateField(blank=True, null=True),
        ),
    ]