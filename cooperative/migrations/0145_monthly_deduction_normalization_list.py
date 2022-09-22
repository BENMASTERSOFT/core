# Generated by Django 4.0.5 on 2022-09-21 05:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0144_monthlyshopdeductionlist_aux'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monthly_Deduction_Normalization_List',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('processed_by', models.CharField(default='ADMIN', max_length=100)),
                ('tdate', models.DateField(default=django.utils.timezone.now)),
                ('transaction_period', models.DateField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('status', models.CharField(choices=[('UNTREATED', 'UNTREATED'), ('TREATED', 'TREATED'), ('ARCHIVED', 'ARCHIVED')], default='UNTREATED', max_length=20)),
                ('cagtegory', models.CharField(choices=[('EQUAL', 'EQUAL'), ('NOT EQUAL', 'NOT EQUAL'), ('DROPPED', 'DROPPED'), ('NEW MEMBER', 'NEW MEMBER')], default='NEW MEMBER', max_length=20)),
                ('processing_status', models.CharField(choices=[('UNPROCESSED', 'UNPROCESSED'), ('PROCESSED', 'PROCESSED')], default='UNPROCESSED', max_length=20)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.members')),
                ('salary_institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.salaryinstitution')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
