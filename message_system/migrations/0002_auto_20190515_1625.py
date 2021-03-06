# Generated by Django 2.1.7 on 2019-05-15 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagerecipient',
            name='recipient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messageRecipient', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='messagerecipient',
            name='recipient_group_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messageGroup', to='message_system.UserGroup'),
            preserve_default=False,
        ),
    ]
