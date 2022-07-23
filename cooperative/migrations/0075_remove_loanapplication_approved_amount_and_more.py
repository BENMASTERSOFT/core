# Generated by Django 4.0.5 on 2022-07-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0074_loanapplication_date_applied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanapplication',
            name='approved_amount',
        ),
        migrations.RemoveField(
            model_name='loanapplicationshortlisting',
            name='nok_Relationship',
        ),
        migrations.RemoveField(
            model_name='loanapplicationshortlisting',
            name='nok_address',
        ),
        migrations.RemoveField(
            model_name='loanapplicationshortlisting',
            name='nok_name',
        ),
        migrations.RemoveField(
            model_name='loanapplicationshortlisting',
            name='nok_phone_no',
        ),
        migrations.RemoveField(
            model_name='loanapplicationshortlisting',
            name='submission_status',
        ),
        migrations.AddField(
            model_name='loanapplicationshortlisting',
            name='approved_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
