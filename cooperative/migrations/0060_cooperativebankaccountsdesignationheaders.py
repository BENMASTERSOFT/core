# Generated by Django 4.0.5 on 2022-07-18 03:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0059_loanlessrepaymentenable'),
    ]

    operations = [
        migrations.CreateModel(
            name='CooperativeBankAccountsDesignationHeaders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('processed_by', models.CharField(default='ADMIN', max_length=100)),
                ('tdate', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]