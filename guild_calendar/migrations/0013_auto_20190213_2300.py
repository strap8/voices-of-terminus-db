# Generated by Django 2.1.7 on 2019-02-14 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guild_calendar', '0012_eventgroupmember_filled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgroupmember',
            name='filled',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventGroupMemberAuthorName', to='user.Character'),
        ),
    ]