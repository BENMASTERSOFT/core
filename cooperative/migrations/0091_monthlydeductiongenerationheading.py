# Generated by Django 3.2.8 on 2022-02-01 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0090_monthlydeductiongenerationheaders'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyDeductionGenerationHeading',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('heading', models.CharField(max_length=255)),
                ('salary_institution', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cooperative.salaryinstitution')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='cooperative.transactionstatus')),
                ('transaction_period', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cooperative.transactionperiods')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
