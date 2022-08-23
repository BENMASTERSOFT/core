# Generated by Django 4.0.5 on 2022-08-23 01:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0114_members_commodity_loan_completed_transactions_phone_no1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members_Commodity_Receipt_Phone_no',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('processed_by', models.CharField(default='ADMIN', max_length=100)),
                ('tdate', models.DateField(default=django.utils.timezone.now)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='INACTIVE', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
