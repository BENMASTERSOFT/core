# Generated by Django 4.0.5 on 2022-07-20 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0082_loanformissuance_date_applied_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequest',
            name='receipt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
