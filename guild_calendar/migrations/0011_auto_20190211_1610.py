# Generated by Django 2.1.2 on 2019-02-12 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guild_calendar', '0010_remove_event_date_modified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='location',
            new_name='locations',
        ),
    ]