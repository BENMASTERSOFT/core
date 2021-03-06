# Generated by Django 4.0.5 on 2022-07-18 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0061_alter_cooperativebankaccountsoperationaldesignations_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperativebankaccountsoperationaldesignations',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.cooperativebankaccounts'),
        ),
        migrations.AlterField(
            model_name='cooperativebankaccountsoperationaldesignations',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.cooperativebankaccountsdesignationheaders'),
        ),
    ]
