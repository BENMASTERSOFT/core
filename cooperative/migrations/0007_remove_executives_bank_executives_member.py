# Generated by Django 4.0.5 on 2022-06-24 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0006_executives_start_date_executives_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='executives',
            name='bank',
        ),
        migrations.AddField(
            model_name='executives',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cooperative.members'),
            preserve_default=False,
        ),
    ]
