# Generated by Django 4.0.5 on 2022-08-10 08:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0097_auxillarydeductions_coop_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity_Loan_Invoicing_Products_Selection_Temp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('processed_by', models.CharField(default='ADMIN', max_length=100)),
                ('tdate', models.DateField(default=django.utils.timezone.now)),
                ('product', models.TextField()),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('quantity', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.members')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]