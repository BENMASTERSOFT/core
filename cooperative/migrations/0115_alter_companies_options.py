# Generated by Django 3.2.8 on 2022-02-08 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0114_companies'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companies',
            options={'ordering': ['title']},
        ),
    ]