# Generated by Django 2.1.1 on 2018-10-09 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20181005_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='tags',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
