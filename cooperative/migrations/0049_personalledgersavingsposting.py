# Generated by Django 4.0.5 on 2022-07-15 06:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0048_commodity_loan_upload_transaction_header_ledger_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalLedgerSavingsPosting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('processed_by', models.CharField(default='ADMIN', max_length=100)),
                ('tdate', models.DateField(default=django.utils.timezone.now)),
                ('particulars', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('status', models.CharField(choices=[('UNTREATED', 'UNTREATED'), ('TREATED', 'TREATED')], default='UNTREATED', max_length=20)),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.membersaccountsdomain')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
