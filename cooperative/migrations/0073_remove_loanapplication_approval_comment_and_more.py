# Generated by Django 4.0.5 on 2022-07-19 15:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0072_alter_loanformissuance_applicant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanapplication',
            name='approval_comment',
        ),
        migrations.RemoveField(
            model_name='loanapplication',
            name='approval_date',
        ),
        migrations.RemoveField(
            model_name='loanapplication',
            name='approval_officer',
        ),
        migrations.RemoveField(
            model_name='loanapplication',
            name='approval_status',
        ),
        migrations.RemoveField(
            model_name='loanapplication',
            name='submission_status',
        ),
        migrations.CreateModel(
            name='LoanApplicationShortListing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('processed_by', models.CharField(default='ADMIN', max_length=100)),
                ('tdate', models.DateField(default=django.utils.timezone.now)),
                ('approval_officer', models.CharField(blank=True, max_length=255, null=True)),
                ('approval_status', models.CharField(choices=[('PENDING', 'PENDING'), ('APPROVED', 'APPROVED')], default='PENDING', max_length=30)),
                ('approval_comment', models.TextField(blank=True, null=True)),
                ('approval_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('UNTREATED', 'UNTREATED'), ('TREATED', 'TREATED')], default='UNTREATED', max_length=20)),
                ('submission_status', models.CharField(choices=[('SUBMITTED', 'SUBMITTED'), ('PENDING', 'PENDING'), ('NOT SUBMITTED', 'NOT SUBMITTED')], default='NOT SUBMITTED', max_length=30)),
                ('nok_name', models.CharField(blank=True, max_length=255, null=True)),
                ('nok_Relationship', models.CharField(blank=True, max_length=255, null=True)),
                ('nok_phone_no', models.CharField(blank=True, max_length=255, null=True)),
                ('nok_address', models.CharField(blank=True, max_length=255, null=True)),
                ('applicant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperative.loanapplication')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
