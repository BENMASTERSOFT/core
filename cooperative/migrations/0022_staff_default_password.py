# Generated by Django 4.0.5 on 2022-07-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0021_xmassavingstransactionperiod'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='default_password',
            field=models.CharField(choices=[('NO', 'NO'), ('YES', 'YES')], default='YES', max_length=10),
        ),
    ]
