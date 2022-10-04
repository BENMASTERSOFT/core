# Generated by Django 4.0.5 on 2022-09-23 21:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0146_rename_cagtegory_monthly_deduction_normalization_list_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalLedgerManualPosting_Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('processed_by', models.CharField(default='ADMIN', max_length=100)),
                ('tdate', models.DateField(default=django.utils.timezone.now)),
                ('account_number', models.CharField(max_length=255)),
                ('particulars', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('transaction_period', models.DateField()),
                ('status', models.CharField(choices=[('UNTREATED', 'UNTREATED'), ('TREATED', 'TREATED'), ('ARCHIVED', 'ARCHIVED')], default='UNTREATED', max_length=20)),
                ('approval_officer', models.CharField(blank=True, max_length=255, null=True)),
                ('approval_status', models.CharField(choices=[('UNPROCESSED', 'UNPROCESSED'), ('PROCESSED', 'PROCESSED')], default='UNPROCESSED', max_length=30)),
                ('approval_comment', models.TextField(blank=True, null=True)),
                ('approval_date', models.DateField(blank=True, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.members')),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperative.transactiontypes')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]