# Generated by Django 2.1.2 on 2019-02-11 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guild_calendar', '0009_auto_20190210_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date_modified',
        ),
    ]
