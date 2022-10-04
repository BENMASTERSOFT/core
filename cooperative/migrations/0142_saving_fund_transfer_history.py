# Generated by Django 4.0.5 on 2022-09-17 15:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0141_transactiontypes_transfer_enabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saving_Fund_Transfer_History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('processed_by', models.CharField(default='ADMIN', max_length=100)),
                ('tdate', models.DateField(default=django.utils.timezone.now)),
                ('sources_account_name', models.CharField(max_length=255)),
                ('sources_accoun_number', models.CharField(max_length=255)),
                ('destination_account_name', models.CharField(max_length=255)),
                ('destination_accoun_number', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('particulars', models.TextField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.members')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]