# Generated by Django 3.2.8 on 2021-12-07 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0002_auto_20211207_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savingsuploaded',
            name='member',
        ),
        migrations.AlterField(
            model_name='savingsuploaded',
            name='transaction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cooperative.membersaccountsdomain'),
        ),
    ]
