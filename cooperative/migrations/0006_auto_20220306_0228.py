# Generated by Django 3.2.8 on 2022-03-06 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0005_auto_20220305_2357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commodity_period_batch',
            old_name='batch',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='commodity_period_batch',
            name='period',
        ),
    ]
