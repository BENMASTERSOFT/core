# Generated by Django 3.2.8 on 2022-02-08 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0115_alter_companies_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.companies')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperative.commodity_product_list')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cooperative.membershipstatus')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
