# Generated by Django 3.2.8 on 2022-02-10 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0124_dedicated_commodity_price_list_dedicated_commodity_product_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dedicated_Commodity_Period',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tyear', models.CharField(max_length=4)),
                ('batch', models.CharField(max_length=10)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cooperative.membershipstatus')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]