# Generated by Django 4.0.5 on 2022-07-19 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0073_remove_loanapplication_approval_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanapplication',
            name='date_applied',
            field=models.DateField(blank=True, null=True),
        ),
    ]
