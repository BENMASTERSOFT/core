# Generated by Django 4.0.5 on 2022-07-04 06:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0020_loansuploaded_admin_charge_rate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='XmasSavingsTransactionPeriod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('processed_by', models.CharField(blank=True, max_length=100, null=True)),
                ('tdate', models.DateField(default=django.utils.timezone.now)),
                ('batch', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=20)),
            ],
            options={
                'db_table': 'XmasSavingsTransactionPeriod',
                'abstract': False,
            },
        ),
    ]
