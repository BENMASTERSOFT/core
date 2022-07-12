# Generated by Django 4.0.5 on 2022-07-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0045_remove_standingorderaccounts_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='standingorderaccounts',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='ACTIVE', max_length=20),
        ),
    ]
