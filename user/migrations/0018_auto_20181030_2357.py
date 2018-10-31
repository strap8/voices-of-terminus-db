# Generated by Django 2.1.1 on 2018-10-31 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20181030_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='create_article',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='create_calendar_event',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='create_newsletter',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_council',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_leader',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_member',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_officer',
            field=models.BooleanField(default=False),
        ),
    ]
