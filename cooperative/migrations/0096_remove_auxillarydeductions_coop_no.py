# Generated by Django 4.0.5 on 2022-08-08 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0095_membersexclusiveness_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auxillarydeductions',
            name='coop_no',
        ),
    ]