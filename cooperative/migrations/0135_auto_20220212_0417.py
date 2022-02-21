# Generated by Django 3.2.8 on 2022-02-12 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0134_remove_essential_commodity_product_selection_summary_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='essential_commodity_product_selection_summary',
            name='duration',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='essential_commodity_product_selection_summary',
            name='transaction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cooperative.transactiontypes'),
            preserve_default=False,
        ),
    ]