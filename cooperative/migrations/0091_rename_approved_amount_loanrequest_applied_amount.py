# Generated by Django 4.0.5 on 2022-08-01 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0090_loanrequest_approved_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanrequest',
            old_name='approved_amount',
            new_name='applied_amount',
        ),
    ]
