# Generated by Django 4.0.5 on 2022-07-20 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0076_loanapplicationshortlisting_processing_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequest',
            name='loan_path',
            field=models.CharField(choices=[('NONE', 'NONE'), ('PROJECT', 'PROJECT'), ('EMERGENCY', 'EMERGENCY')], default='PROJECT', max_length=20),
        ),
    ]
