# Generated by Django 3.2.8 on 2022-02-07 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0103_commodity_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity_category',
            name='transaction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cooperative.transactiontypes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commodity_category',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]