# Generated by Django 4.0.5 on 2022-06-24 10:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0005_executivepositions_executives'),
    ]

    operations = [
        migrations.AddField(
            model_name='executives',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='executives',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='INACTIVE', max_length=20),
        ),
        migrations.AddField(
            model_name='executives',
            name='stop_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
