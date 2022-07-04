# Generated by Django 4.0.5 on 2022-06-30 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0013_loansrepaymentbase_guarantor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loanguarantors',
            old_name='guarantor',
            new_name='member',
        ),
        migrations.RemoveField(
            model_name='loanguarantors',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='loansrepaymentbase',
            name='guarantor',
        ),
        migrations.AddField(
            model_name='loanguarantors',
            name='loan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperative.loansrepaymentbase'),
        ),
    ]