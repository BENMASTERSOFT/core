# Generated by Django 3.2.8 on 2022-01-29 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0085_auto_20220129_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactiontypes',
            name='form_print',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cooperative.yesno'),
        ),
    ]