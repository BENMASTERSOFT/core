# Generated by Django 4.0.5 on 2022-07-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0055_auxillarydeductions'),
    ]

    operations = [
        migrations.AddField(
            model_name='auxillarydeductions',
            name='coop_no',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
