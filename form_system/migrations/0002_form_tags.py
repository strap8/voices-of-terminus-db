# Generated by Django 2.1.7 on 2019-05-08 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='tags',
            field=models.CharField(default='Form', max_length=512),
        ),
    ]
