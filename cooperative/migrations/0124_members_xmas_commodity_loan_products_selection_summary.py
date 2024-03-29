# Generated by Django 4.0.5 on 2022-08-29 08:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0123_members_xmas_commodity_loan_products_selection_selection_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members_Xmas_Commodity_Loan_Products_Selection_Summary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('processed_by', models.CharField(default='ADMIN', max_length=100)),
                ('tdate', models.DateField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('interest', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('ticket', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('status', models.CharField(choices=[('UNTREATED', 'UNTREATED'), ('TREATED', 'TREATED'), ('ARCHIVED', 'ARCHIVED')], default='UNTREATED', max_length=20)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.members')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
