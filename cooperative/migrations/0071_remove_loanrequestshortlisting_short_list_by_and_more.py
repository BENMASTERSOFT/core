# Generated by Django 4.0.5 on 2022-07-19 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0070_remove_loanrequest_short_list_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanrequestshortlisting',
            name='short_list_by',
        ),
        migrations.RemoveField(
            model_name='loanrequestshortlisting',
            name='short_listed_date',
        ),
    ]
