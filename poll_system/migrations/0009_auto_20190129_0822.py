# Generated by Django 2.1.2 on 2019-01-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll_system', '0008_auto_20190128_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollresponse',
            name='response',
            field=models.TextField(blank=True, null=True),
        ),
    ]