# Generated by Django 3.2.8 on 2022-01-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0025_compulsorysavings'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooperativeshopledger',
            name='receipt',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
